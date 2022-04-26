import pandas as pd
import numpy as np

import core
import const

def get_mark_wide(df):
    """
    Return mark in wide format
    
    Args:
        df: attendee left join with response

    Returns:
        A DataFrame
    """
    df1 = (
        pd.pivot(
            df,
            index=['user_id', 'name_last', 'name_first', 'note', 'class_id', 'course_id'], 
            columns='exam_id',
            values='mark')
        .reset_index()
        .rename_axis(None, axis=1)
    )
    return df1

def get_CC_columns(columns):
    return [c for c in columns if '-CC' in str(c)]

def get_QT_columns(columns):
    return [c for c in columns[6:] if '-QT' in str(c)]

def get_THI1_columns(columns):
    # print([c for c in columns[6:] if '-THI1' in str(c) or 'VT1' in str(c)])
    return ['VT1', 'VP1'] + [c for c in columns[6:] if '-THI1' in str(c)]

def get_TB1_columns(columns):
    lst = ['CC', 'QT', 'THI1']
    return [c for c in columns[6:] if c in lst]

def get_NOTE1_columns(columns):
    lst = ['VT1', 'VP1', 'THI1', 'TB1']
    return [c for c in columns[6:] if c in lst]

def get_THI1_PRINT_columns(columns):
    lst = ['VT1', 'VP1', 'THI1']
    return [c for c in columns[6:] if c in lst]

def get_THI2_columns(columns):
    # print([c for c in columns[6:] if '-THI2' in str(c) or 'VT2' in str(c)])
    return ['VT2', 'VP2'] + [c for c in columns[6:] if '-THI2' in str(c)]

def get_TB2_columns(columns):
    lst = ['CC', 'QT', 'THI2']
    return [c for c in columns[6:] if c in lst]

def get_NOTE2_columns(columns):
    lst = ['VT2', 'VP2', 'THI2', 'TB2']
    return [c for c in columns[6:] if c in lst]

def get_THI2_PRINT_columns(columns):
    lst = ['VT2', 'VP2', 'THI2']
    return [c for c in columns[6:] if c in lst]


def calc_CC(row, method='mean'):
    if len(row) == 0:
        return 0
    elif method == 'max':
        return core.round_half_up(np.max(row.fillna(0)))
    else:
        return core.round_half_up(np.mean(row.fillna(0)))

def calc_QT(row, method='mean'):
    if len(row) == 0:
        return 0
    elif method == 'max':
        return core.round_half_up(np.max(row.fillna(0)))
    else:
        return core.round_half_up(np.mean(row.fillna(0)))

def calc_VT_VP(row, lst):
    return row[0] in lst

def calc_THI1(row):
    # Khong co bai nhung co diem danh: 0
    if not row[2] and not row[0]:
        return 0
    else:
        return row[2]

def calc_THI1_PRINT(row):
    # 'VT1', 'VP1', 'THI1'
    # Khong co bai nhung co diem danh: 0
    vt, vp, thi = row[0], row[1], row[2]
    if pd.isna(thi) and not vt:
        return 0
    elif pd.isna(thi) and vt and not vp:
        return 'VT'
    elif pd.isna(thi) and vt and vp:
        return 'VP'
    else:
        return thi

def calc_TB1(row):
    row = row.fillna(0)
    grade = (10 * row[0] + 20 * row[1] + 70 * row[2]) / 100
    return core.round_half_up(round(grade, 2), 1)

def calc_NOTE1(row):
    # 'VT1', 'VP1', 'THI1', 'TB1'
    vt, vp, thi, tb = row[0], row[1], row[2], row[3]
    if vt and not vp:
        return 'VT'
    elif vt and vp:
        return 'VP'
    elif thi >= 5 and tb >= 4:
        return ''
    elif thi < 5 or tb < 4:
        return 'Rớt'
    else:
        return 'PENDING'

def calc_THI2(row):
    # VT2, VP2, THI2
    # Khong co bai nhung co diem danh: 0
    if not row[2] and not row[0]:
        return 0
    else:
        return row[2]

def calc_THI2_PRINT(row):
    # 'VT2', 'VP2', 'THI2'
    # Khong co bai nhung co diem danh: 0
    vt, vp, thi = row[0], row[1], row[2]
    if pd.isna(thi) and not vt:
        return 0
    elif pd.isna(thi) and vt and not vp:
        return 'VT'
    elif pd.isna(thi) and vt and vp:
        return 'VP'
    else:
        return thi

def calc_TB2(row):
    row = row.fillna(0)
    grade = (10 * row[0] + 20 * row[1] + 70 * row[2]) / 100
    return core.round_half_up(round(grade, 2), 1)

def calc_NOTE2(row):
    # 'VT2', 'VP2', 'THI2', 'TB2'
    vt, vp, thi, tb = row[0], row[1], row[2], row[3]
    if vt and not vp:
        return 'VT'
    elif vt and vp:
        return 'VP'
    elif thi >= 5 and tb >= 4:
        return ''
    elif thi < 5 or tb < 4:
        return 'Rớt'
    else:
        return 'PENDING'


def calc(response, attendee, course_id='', vt_vp={
        'vt1': [], 'vp1': [], 'vt2': [], 'vp2': [],
    }):
    df = (attendee
        .merge(response, left_on='user_id', right_on='user_id', how='left')
    )

    dfw = get_mark_wide(df)

    # Tao cot CC, QT
    if (course_id + '-CC1') not in dfw.columns:
        dfw[course_id + '-CC1'] = np.nan
    if (course_id + '-QT1') not in dfw.columns:
        dfw[course_id + '-QT1'] = np.nan

    # Tao cot thi lan 1, 2
    if (course_id + '-THI1') not in dfw.columns:
        dfw[course_id + '-THI1'] = np.nan
    if (course_id + '-THI2') not in dfw.columns:
        dfw[course_id + '-THI2'] = np.nan

    dfw['CC'] = dfw[get_CC_columns(dfw.columns)].apply(calc_CC, axis = 1)
    dfw['QT'] = dfw[get_QT_columns(dfw.columns)].apply(calc_QT, axis = 1)
    dfw['VT1'] = dfw.apply(calc_VT_VP, args=(vt_vp['vt1'],) , axis=1)
    dfw['VP1'] = dfw.apply(calc_VT_VP, args=(vt_vp['vp1'],) , axis=1)
    dfw['THI1'] = dfw[get_THI1_columns(dfw.columns)].apply(calc_THI1, axis = 1)
    dfw['TB1'] = dfw[get_TB1_columns(dfw.columns)].apply(calc_TB1, axis=1)
    dfw['THI1_PRINT'] = dfw[get_THI1_PRINT_columns(dfw.columns)].apply(calc_THI1_PRINT, axis = 1)
    dfw['NOTE1'] = dfw[get_NOTE1_columns(dfw.columns)].apply(calc_NOTE1, axis=1)
    dfw['VT2'] = dfw.apply(calc_VT_VP, args=(vt_vp['vt2'],) , axis=1)
    dfw['VP2'] = dfw.apply(calc_VT_VP, args=(vt_vp['vp2'],) , axis=1)
    dfw['THI2'] = dfw[get_THI2_columns(dfw.columns)].apply(calc_THI2, axis = 1)
    dfw['TB2'] = dfw[get_TB2_columns(dfw.columns)].apply(calc_TB2, axis=1)
    dfw['THI2_PRINT'] = dfw[get_THI2_PRINT_columns(dfw.columns)].apply(calc_THI2_PRINT, axis = 1)
    dfw['NOTE2'] = dfw[get_NOTE2_columns(dfw.columns)].apply(calc_NOTE2, axis=1)
    return dfw

