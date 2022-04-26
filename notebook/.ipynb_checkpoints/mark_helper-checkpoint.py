import pandas as pd
import numpy as np
from pathlib import Path
import re
import util


def get_mark(df, cutpoint, total, exam_id='exam_id'):
    """
    Return mark by merge_asof with cutpoint
    
    df: data frame with 2 col 'mssv' and 'scd'
    total: interger, total points
    exam_id: string, exam_id, to rename column
    """
    df['pct_score'] = df['score'] / total
    df['pct_score'] = df['pct_score'].astype('float')
    df = df.groupby('user_id').agg('max').reset_index()
    df1 = pd.merge_asof(
        df.sort_values(by='pct_score'),
        cutpoint,
        on='pct_score'
    ).set_index('user_id').rename_axis('user_id')
    df1['exam_id'] = exam_id
    df1 = df1.rename(columns={
        'score': 'score_' + str(exam_id)
    })
    df1 = df1.reset_index()
    return df1[['user_id', 'class_id', 'course_id', 'exam_id', 'mark']]


def set_score(data, df):
    row = pd.DataFrame([data], columns=df.columns)
    return pd.concat([df.copy(), row], ignore_index=True)


def get_mark_wide(df):
    """
    Return mark in wide format
    
    df: parsed response
    """
    df1 = (
        pd.pivot(df, index=['user_id', 'class_id', 'course_id'], columns='exam_id', values='mark')
        .reset_index()
        .rename_axis(None, axis=1)
    )
    return df1


def get_mark_long(df, value_vars=[]):
    df1 = (
        pd
        .melt(
            df,
            id_vars=['user_id', 'class_id', 'course_id'],
            value_vars=value_vars)
        .rename(columns={
            'variable': 'exam_id',
            'value': 'mark'
        })
    )
    return df1


def mask_mark(row):
    if not np.isnan(row[0]):
        return row[0]
    elif np.isnan(row[1]) or np.isnan(row[2]):
        return 'VT'
    elif row[1] and not row[2]:
        return 'VT'
    elif row[1] and row[2]:
        return 'VP'

def get_mark_xstk_1(attendee, examinee, vp1=[], vp2=[]):
    df = attendee[['user_id', 'name_last', 'name_first', 'note']]
    cc = (
        examinee
        .query('exam_category == "cc"')
        [['user_id', 'mark']]
        .fillna(0)
        .groupby('user_id')
        .mean()
        .round(1)
        .rename(columns={'mark': 'cc'})
    )
    qt = (
        examinee
        .query('exam_category == "qt"')
        [['user_id', 'mark']]
        .groupby('user_id')
        .mean()
        .round(1)
        .rename(columns={'mark': 'qt'})
    )
    thi1 = (
        examinee
        .query('exam_category == "thi1"')
        [['user_id', 'mark']]
        .groupby('user_id')
        .max()
        .round(1)
        .rename(columns={'mark': 'thi1'})
    )
    thi2 = (
        examinee
        .query('exam_category == "thi2"')
        [['user_id', 'mark']]
        .groupby('user_id')
        .max()
        .rename(columns={'mark': 'thi2'})
    )
    df1 = (
        df
        .merge(cc, left_on='user_id', right_on='user_id', how='left')
        .merge(qt, left_on='user_id', right_on='user_id', how='left')
        .merge(thi1, left_on='user_id', right_on='user_id', how='left')
        .merge(thi2, left_on='user_id', right_on='user_id', how='left')
        # .merge(v1, left_on='user_id', right_on='user_id', how='left')
        # .merge(v2, left_on='user_id', right_on='user_id', how='left')
    )
    df1['vt1'] = np.isnan(df1['thi1'])
    df1['vp1'] = False
    df1['vt2'] = np.isnan(df1['thi2'])
    df1['vp2'] = False
    
    for e in vp1:
        df1.loc[df1.user_id == e, 'vp1'] = True
    for e in vp2:
        df1.loc[df1.user_id == e, 'vp2'] = True
        
    df1['cc_masked'] = df1['cc'].fillna(0)
    df1['qt_masked'] = df1['qt'].fillna(0)
    df1['thi1_masked'] = df1[['thi1', 'vt1', 'vp1']].apply(mask_mark, axis=1)
    df1['thi2_masked'] = df1[['thi2', 'vt2', 'vp2']].apply(mask_mark, axis=1)
    df1['tb1'] = (
        0.1 * df1['cc'].fillna(0)
        + 0.2 * df1['qt'].fillna(0)
        + 0.7 * df1['thi1'].fillna(0)
    ).round(1)
    df1['tb2'] = (
        0.1 * df1['cc'].fillna(0)
        + 0.2 * df1['qt'].fillna(0)
        + 0.7 * df1['thi2'].fillna(0)
    ).round(1)
    df1['quamon1'] = (df1['thi1'].fillna(0) >= 5) & (df1['tb1'] >= 4)
    df1['quamon2'] = (df1['thi2'].fillna(0) >= 5) & (df1['tb2'] >= 4)
    conditions1 = [
        ((df1['vt1'] == True) & (df1['vp1'] == False)),
        ((df1['vt1'] == True) & (df1['vp1'] == True)),
        (df1['quamon1'] == False),
        (df1['quamon1'] == True)
    ]
    values1 = ['Vắng thi', 'Vắng phép', 'Rớt', '']
    df1['note1'] = np.select(conditions1, values1)
    conditions2 = [
        ((df1['vt2'] == True) & (df1['vp2'] == False)),
        ((df1['vt2'] == True) & (df1['vp2'] == True)),
        (df1['quamon2'] == False),
        (df1['quamon2'] == True)
    ]
    values2 = ['Vắng thi', 'Vắng phép', 'Rớt', '']
    df1['note2'] = np.select(conditions2, values2)
    return df1


def get_mark_INFO1001_1(attendee, examinee, vplt1=[], vplt2=[], vpth1=[], vpth2=[]):
    """
    Tinh diem mon INFO1001, procedure 1
    """
    df = attendee[['user_id', 'name_last', 'name_first', 'note']]
    cc = (
        examinee
        .query('exam_category == "cc"')
        [['user_id', 'mark']]
        .fillna(0)
        .groupby('user_id')
        .mean()
        .round(1)
        .rename(columns={'mark': 'cc'})
    )
    qt = (
        examinee
        .query('exam_category == "qt"')
        [['user_id', 'mark']]
        .groupby('user_id')
        .mean()
        .round(1)
        .rename(columns={'mark': 'qt'})
    )
    thilt1 = (
        examinee
        .query('exam_category == "thilt1"')
        [['user_id', 'mark']]
        .groupby('user_id')
        .max()
        .round(1)
        .rename(columns={'mark': 'thilt1'})
    )
    thilt2 = (
        examinee
        .query('exam_category == "thilt2"')
        [['user_id', 'mark']]
        .groupby('user_id')
        .max()
        .rename(columns={'mark': 'thilt2'})
    )
    thith1 = (
        examinee
        .query('exam_category == "thith1"')
        [['user_id', 'mark']]
        .groupby('user_id')
        .max()
        .round(1)
        .rename(columns={'mark': 'thith1'})
    )
    thith2 = (
        examinee
        .query('exam_category == "thith2"')
        [['user_id', 'mark']]
        .groupby('user_id')
        .max()
        .rename(columns={'mark': 'thith2'})
    )
    df1 = (
        df
        .merge(cc, left_on='user_id', right_on='user_id', how='left')
        .merge(qt, left_on='user_id', right_on='user_id', how='left')
        .merge(thilt1, left_on='user_id', right_on='user_id', how='left')
        .merge(thith1, left_on='user_id', right_on='user_id', how='left')
        .merge(thilt2, left_on='user_id', right_on='user_id', how='left')
        .merge(thith2, left_on='user_id', right_on='user_id', how='left')
    )
    
    
    
    # Tao cot vang thi
    df1['vtlt1'] = np.isnan(df1['thilt1'])
    df1['vplt1'] = False
    df1['vtlt2'] = np.isnan(df1['thilt2'])
    df1['vplt2'] = False
    df1['vtth1'] = np.isnan(df1['thith1'])
    df1['vpth1'] = False
    df1['vtth2'] = np.isnan(df1['thith2'])
    df1['vpth2'] = False
    
    # Xu ly SV vang co phep
    for e in vplt1:
        df1.loc[df1.user_id == e, 'vplt1'] = True
    for e in vplt2:
        df1.loc[df1.user_id == e, 'vplt2'] = True
    for e in vpth1:
        df1.loc[df1.user_id == e, 'vpth1'] = True
    for e in vpth2:
        df1.loc[df1.user_id == e, 'vpth2'] = True
    
    # replace: Vang CC, QT --> 0 diem
    df1['cc_masked'] = df1['cc'].fillna(0)
    df1['qt_masked'] = df1['qt'].fillna(0)
    
    # TODO: Tinh diem lan 2
    
    # replace: vang thi
    df1['thilt1_masked'] = df1[['thilt1', 'vtlt1', 'vplt1']].apply(mask_mark, axis=1)
    df1['thilt2_masked'] = df1[['thilt2', 'vtlt2', 'vplt2']].apply(mask_mark, axis=1)
    df1['thith1_masked'] = df1[['thith1', 'vtth1', 'vpth1']].apply(mask_mark, axis=1)
    df1['thith2_masked'] = df1[['thith2', 'vtth2', 'vpth2']].apply(mask_mark, axis=1)
    
    # Tinh diem tb: round_half_up
    df1['tb1'] = (util.round_half_up(
        (0.1 * df1['cc'].fillna(0)
        + 0.2 * df1['qt'].fillna(0)
        + 0.42 * df1['thilt1'].fillna(0)
        + 0.28 * df1['thith1'].fillna(0)), 1
    ))
    df1['tb2'] = (util.round_half_up(
        (0.1 * df1['cc'].fillna(0)
        + 0.2 * df1['qt'].fillna(0)
        + 0.42 * df1['thilt2'].fillna(0)
        + 0.28 * df1['thith2'].fillna(0)), 1
    ))
    
    # Tao cac cot qua mon lt, th, qua ca 2
    df1['quamonlt1'] = (df1['thilt1'].fillna(0) >= 5)
    df1['quamonlt2'] = (df1['thilt2'].fillna(0) >= 5)
    df1['quamonth1'] = (df1['thith1'].fillna(0) >= 5)
    df1['quamonth2'] = (df1['thith2'].fillna(0) >= 5)
    df1['quamon1'] = (
        (df1['thilt1'].fillna(0) >= 5)
        & (df1['thith1'].fillna(0) >= 5)
        & (df1['tb1'] >= 4))
    df1['quamon2'] = (
        (df1['thilt2'].fillna(0) >= 5)
        & (df1['thith2'].fillna(0) >= 5)
        & (df1['tb2'] >= 4))
    
    # Ghi chu 1
    conditions1 = [
        ((df1['vtlt1'] == True) & (df1['vplt1'] == False) & (df1['vtth1'] == False) & (df1['vpth1'] == False)),
        ((df1['vtlt1'] == True) & (df1['vplt1'] == True) & (df1['vtth1'] == False) & (df1['vpth1'] == False)),
        ((df1['vtlt1'] == False) & (df1['vplt1'] == False) & (df1['vtth1'] == True) & (df1['vpth1'] == False)),
        ((df1['vtlt1'] == False) & (df1['vplt1'] == False) & (df1['vtth1'] == True) & (df1['vpth1'] == True)),
        ((df1['vtlt1'] == True) & (df1['vplt1'] == False) & (df1['vtth1'] == True) & (df1['vpth1'] == False)),
        ((df1['vtlt1'] == True) & (df1['vplt1'] == True) & (df1['vtth1'] == True) & (df1['vpth1'] == False)),
        ((df1['vtlt1'] == True) & (df1['vplt1'] == False) & (df1['vtth1'] == True) & (df1['vpth1'] == True)),
        ((df1['vtlt1'] == True) & (df1['vplt1'] == True) & (df1['vtth1'] == True) & (df1['vpth1'] == True)),
        ((df1['quamonlt1'] == False) & (df1['quamonth1'] == False)),
        ((df1['quamonlt1'] == True) & (df1['quamonth1'] == False)),
        ((df1['quamonlt1'] == False) & (df1['quamonth1'] == True)),
        ((df1['quamonlt1'] == True) & (df1['quamonth1'] == True)),
    ]
    values1 = ['VT LT', 'VP LT', 'VT TH', 'VP TH',
               'VT LT, VT TH', 'VP LT, VT TH', 'VT LT, VP TH', 'VP LT, VP TH',
               'Rớt LT, TH', 'Rớt TH', 'Rớt LT', '']
    df1['note1'] = np.select(conditions1, values1)
    # Ghi chu 2
    conditions2 = [
        ((df1['vtlt2'] == True) & (df1['vplt2'] == False) & (df1['vtth2'] == False) & (df1['vpth2'] == False)),
        ((df1['vtlt2'] == True) & (df1['vplt2'] == True) & (df1['vtth2'] == False) & (df1['vpth2'] == False)),
        ((df1['vtlt2'] == False) & (df1['vplt2'] == False) & (df1['vtth2'] == True) & (df1['vpth2'] == False)),
        ((df1['vtlt2'] == False) & (df1['vplt2'] == False) & (df1['vtth2'] == True) & (df1['vpth2'] == True)),
        ((df1['vtlt2'] == True) & (df1['vplt2'] == False) & (df1['vtth2'] == True) & (df1['vpth2'] == False)),
        ((df1['vtlt2'] == True) & (df1['vplt2'] == True) & (df1['vtth2'] == True) & (df1['vpth2'] == False)),
        ((df1['vtlt2'] == True) & (df1['vplt2'] == False) & (df1['vtth2'] == True) & (df1['vpth2'] == True)),
        ((df1['vtlt2'] == True) & (df1['vplt2'] == True) & (df1['vtth2'] == True) & (df1['vpth2'] == True)),
        ((df1['quamonlt2'] == False) & (df1['quamonth2'] == False)),
        ((df1['quamonlt2'] == True) & (df1['quamonth2'] == False)),
        ((df1['quamonlt2'] == False) & (df1['quamonth2'] == True)),
        ((df1['quamonlt2'] == True) & (df1['quamonth2'] == True)),
    ]
    values2 = ['VT LT', 'VP LT', 'VT TH', 'VP TH',
               'VT LT, VT TH', 'VP LT, VT TH', 'VT LT, VP TH', 'VP LT, VP TH',
               'Rớt LT, TH', 'Rớt TH', 'Rớt LT', '']
    df1['note2'] = np.select(conditions2, values2)
    return df1
