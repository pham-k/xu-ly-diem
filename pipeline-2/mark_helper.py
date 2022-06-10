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

# get input columns
def get_CC_columns(columns):
    return [c for c in columns if '-CC' in str(c)]

def get_QT_columns(columns):
    return [c for c in columns[6:] if '-QT' in str(c)]

def get_THILT1_columns(columns):
    # print([c for c in columns[6:] if '-THI1' in str(c) or 'VT1' in str(c)])
    return ['VTLT1', 'VPLT1'] + [c for c in columns[6:] if '-THILT1' in str(c)]

def get_THITH1_columns(columns):
    # print([c for c in columns[6:] if '-THI1' in str(c) or 'VT1' in str(c)])
    return ['VTTH1', 'VPTH1'] + [c for c in columns[6:] if '-THITH1' in str(c)]

def get_THILT2_columns(columns):
    # print([c for c in columns[6:] if '-THILT2' in str(c)])
    return ['VTLT2', 'VPLT2'] + [c for c in columns[6:] if '-THILT2' in str(c)]

def get_THITH2_columns(columns):
    # print([c for c in columns[6:] if '-THI1' in str(c) or 'VT1' in str(c)])
    return ['VTTH2', 'VPTH2'] +[c for c in columns[6:] if '-THITH2' in str(c)]

def get_TB1_columns(columns):
    lst = ['CC', 'QT', 'THILT1', 'THITH1']
    return lst

def get_TB2_columns(columns):
    lst = ['CC', 'QT', 'THILT1', 'THITH1', 'THILT2', 'THITH2']
    return lst

def get_NOTE1_columns(columns):
    lst = ['VTLT1', 'VPLT1', 'VTTH1', 'VPTH1', 'THILT1', 'THITH1', 'TB1']
    return lst

def get_NOTE2_columns(columns):
    lst = ['VTLT2', 'VPLT2', 'VTTH2', 'VPTH2', 'THILT1', 'THITH1', 'THILT2', 'THITH2', 'TB2']
    return lst

def get_THILT1_PRINT_columns(columns):
    lst = ['VTLT1', 'VPLT1', 'THILT1']
    # return [c for c in columns[6:] if c in lst]
    return lst

def get_THITH1_PRINT_columns(columns):
    lst = ['VTTH1', 'VPTH1', 'THITH1']
    # return [c for c in columns[6:] if c in lst]
    return lst

# Calculate
def calc_CC(row, method='mean'):
    if method == 'max':
        return core.round_half_up(np.max(row.fillna(0)))
    else:
        return core.round_half_up(np.mean(row.fillna(0)))

def calc_QT(row, method='mean'):
    if method == 'max':
        return core.round_half_up(np.max(row.fillna(0)))
    else:
        return core.round_half_up(np.mean(row.fillna(0)))

# Thi lan 1
def calc_VT_VP(row, lst):
    return row[0] in lst

def calc_THILT1(row):
    # Khong co bai nhung co diem danh: 0
    if not row[2] and not row[0]:
        return 0
    else:
        return row[2]

def calc_THITH1(row):
    # Khong co bai nhung co diem danh: 0
    if not row[2] and not row[0]:
        return 0
    else:
        return row[2]

# Thi lan 2
def calc_THILT2(row):
    # Khong co bai nhung co diem danh: 0
    if not row[2] and not row[0]:
        return 0
    else:
        return row[2]

def calc_THITH2(row):
    # Khong co bai nhung co diem danh: 0
    if not row[2] and not row[0]:
        return 0
    else:
        return row[2]

# ?
def calc_THILT1_PRINT(row):
    # 'VTLT1', 'VPLT1', 'THILT1'
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

def calc_THITH1_PRINT(row):
    # 'VTTH1', 'VPTH1', 'THITH1'
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

def calc_THILT2_PRINT(row):
    # 'VTLT2', 'VPLT2', 'THILT1', 'THILT2'
    
    vtlt2, vplt2, thilt1, thilt2 = row[0], row[1], row[2], row[3]
    if pd.notna(thilt2):
        return thilt2
    elif pd.notna(thilt1) and pd.isna(thilt2) and vtlt2 and not vplt2 and thilt1 < 5:
        return 'VT'
    elif pd.notna(thilt1) and pd.isna(thilt2):
        return thilt1
    elif pd.isna(thilt1) and pd.isna(thilt2) and vplt2:
        return 'VP'
    elif pd.isna(thilt1) and pd.isna(thilt2) and vtlt2 and not vplt2:
        return 'VT'
    elif pd.isna(thilt1) and pd.isna(thilt2) and not vtlt2 and not vplt2:
        return 'VT'
    
    else:
        return 'PENDING'

def calc_THITH2_PRINT(row):
    # 'VTTH2', 'VPTH2', 'THITH1', 'THITH2'
    
    vtth2, vpth2, thith1, thith2 = row[0], row[1], row[2], row[3]
    if pd.notna(thith2):
        return thith2
    elif pd.notna(thith1) and pd.isna(thith2):
        return thith1
    elif pd.isna(thith1) and pd.isna(thith2) and vpth2:
        return 'VP'
    elif pd.isna(thith1) and pd.isna(thith2) and vtth2 and not vpth2:
        return 'VT'
    elif pd.isna(thith1) and pd.isna(thith2) and not vtth2 and not vpth2:
        return 'VT'
    else:
        return 'PENDING'


def calc_TB1(row):
    row = row.fillna(0)
    cc, qt, thilt, thith = row[0], row[1], row[2], row[3]
    grade = (10 * cc + 20 * qt + 42 * thilt + 28 * thith) / 100
    return core.round_half_up(round(grade, 2), 1)

def calc_TB2(row):
    # 'CC', 'QT', 'THILT1', 'THITH1', 'THILT2', 'THITH2'
    row = row.fillna(0)
    cc, qt, thilt1, thith1, thilt2, thith2 = row[0], row[1], row[2], row[3], row[4], row[5]
    thilt = max(thilt1, thilt2)
    thith = max(thith1, thith2)
    grade = (10 * cc + 20 * qt + 42 * thilt + 28 * thith) / 100
    return core.round_half_up(round(grade, 2), 1)

def calc_NOTE1(row):
    # 'VTLT1', 'VPLT1', 'VTTH1', 'VPTH1', 'THILT1', 'THITH1', 'TB1'
    vtlt1, vplt1, vtth1, vpth1, thilt1, thith1, tb1 = row[0], row[1], row[2], row[3], row[4], row[5], row[6]
    # Vang thi
    if vtlt1 and vtth1 and not vplt1 and not vpth1:
        return 'VT LT, VT TH'
    elif vtlt1 and vtth1 and vplt1 and not vpth1:
        return 'VP LT, VT TH'
    elif vtlt1 and vtth1 and not vplt1 and vpth1:
        return 'VT LT, VP TH'
    elif vtlt1 and vtth1 and vplt1 and vpth1:
        return 'VP LT, VP TH'
    # Dau
    elif thilt1 >= 5 and thith1 >= 5 and tb1 >= 4:
        return ''
    # Rot
    elif thilt1 < 5 and thith1 >= 5:
        return 'Rớt LT'
    elif not vtlt1 and pd.isna(thilt1) and thith1 >= 5:
        return 'Rớt LT'
    elif thilt1 >= 5 and thith1 < 5:
        return 'Rớt TH'
    elif not vtth1 and pd.isna(thith1) and thilt1 >= 5:
        return 'Rớt TH'
    elif thilt1 < 5 and thith1 < 5:
        return 'Rớt LT, TH'
    elif not vtlt1 and not vtth1 and pd.isna(thilt1) and pd.isna(thith1):
        return 'Rớt LT, TH'
    elif not vtlt1 and not vtth1 and thilt1 < 5 and pd.isna(thith1):
        return 'Rớt LT, TH'
    elif tb1 < 4:
        return 'Rớt'
    # ??
    else:
        return 'PENDING'

def calc_NOTE2(row):
    # 'VTLT2', 'VPLT2', 'VTTH2', 'VPTH2', 'THILT1', 'THITH2', 'THILT2', 'THITH2', 'TB2'
    vtlt2, vplt2, vtth2, vpth2 = row[0], row[1], row[2], row[3]
    thilt1, thith1, thilt2, thith2 = row[4], row[5], row[6], row[7]
    tb2 = row[8]

    # Dau
    if ((thilt1 >= 5 or thilt2 >= 5)
        and (thith1 >= 5 or thith2 >= 5)
        and tb2 >= 4):
        return ''
    # Vang thi
    # Vang thi
    elif vtlt2 and vtth2 and not vplt2 and not vpth2:
        return 'VT LT, VT TH'
    elif vtlt2 and vtth2 and vplt2 and not vpth2:
        return 'VP LT, VT TH'
    elif vtlt2 and vtth2 and not vplt2 and vpth2:
        return 'VT LT, VP TH'
    elif vtlt2 and vtth2 and vplt2 and vpth2:
        return 'VP LT, VP TH'
    # elif (pd.isna(thilt1) and pd.isna(thith1)
    #     and pd.isna(thilt2) and pd.isna(thith2)
    #     and not vplt2 and not vpth2):
    #     return 'VT LT, VT TH'
    # Rot
    elif (pd.notna(thilt2) and thilt2 < 5 and pd.notna(thith2) and thith2 < 5):
        return 'Rớt LT, TH'
    elif pd.notna(thilt2) and thilt2 < 5:
        return 'Rớt LT'
    elif pd.notna(thith2) and thith2 < 5:
        return 'Rớt TH'
    elif tb2 < 4:
        return 'Rớt'
    else:
        return 'PENDING'
    
def calc(
    response, attendee,
    course_id='INFO1001-2021-KX-1',
    vt_vp={
        'vtlt1': [], 'vplt1': [], 'vtth1': [], 'vpth1': [],
        'vtlt2': [], 'vplt2': [], 'vtth2': [], 'vpth2': [],
    }):
    df = (attendee
        .merge(response, left_on='user_id', right_on='user_id', how='left')
    )
    dfw = get_mark_wide(df)
    # Tao cot CC1
    if (course_id + '-CC1') not in dfw.columns:
        dfw[course_id + '-CC1'] = np.nan
    # Tao cot CC2
    if (course_id + '-CC2') not in dfw.columns:
        dfw[course_id + '-CC2'] = np.nan
    # Tao cot CC3
    if (course_id + '-CC3') not in dfw.columns:
        dfw[course_id + '-CC3'] = np.nan
    # Tao cot QT1
    if (course_id + '-QT1') not in dfw.columns:
        dfw[course_id + '-QT1'] = np.nan

    # Tao cot thi lan 1
    if (course_id + '-THILT1') not in dfw.columns:
        dfw[course_id + '-THILT1'] = np.nan
    if (course_id + '-THITH1') not in dfw.columns:
        dfw[course_id + '-THITH1'] = np.nan

    # Tao cot thi lan 2
    if (course_id + '-THILT2') not in dfw.columns:
        dfw[course_id + '-THILT2'] = np.nan
    if (course_id + '-THITH2') not in dfw.columns:
        dfw[course_id + '-THITH2'] = np.nan

    dfw['CC'] = dfw[get_CC_columns(dfw.columns)].apply(calc_CC, axis = 1)
    dfw['QT'] = dfw[get_QT_columns(dfw.columns)].apply(calc_QT, axis = 1)
    
    # thi lan 1
    dfw['VTLT1'] = dfw.apply(calc_VT_VP, args=(vt_vp['vtlt1'],), axis=1)
    dfw['VPLT1'] = dfw.apply(calc_VT_VP, args=(vt_vp['vplt1'],), axis=1)
    dfw['THILT1'] = dfw[get_THILT1_columns(dfw.columns)].apply(calc_THILT1, axis = 1)
    
    dfw['VTTH1'] = dfw.apply(calc_VT_VP, args=(vt_vp['vtth1'],),axis=1)
    dfw['VPTH1'] = dfw.apply(calc_VT_VP, args=(vt_vp['vpth1'],),axis=1)
    dfw['THITH1'] = dfw[get_THITH1_columns(dfw.columns)].apply(calc_THITH1, axis = 1)

    # thi lan 
    dfw['VTLT2'] = dfw.apply(calc_VT_VP, args=(vt_vp['vtlt2'],), axis=1)
    dfw['VPLT2'] = dfw.apply(calc_VT_VP, args=(vt_vp['vplt2'],), axis=1)
    dfw['THILT2'] = dfw[get_THILT2_columns(dfw.columns)].apply(calc_THILT2, axis = 1)
    
    dfw['VTTH2'] = dfw.apply(calc_VT_VP, args=(vt_vp['vtth2'],), axis=1)
    dfw['VPTH2'] = dfw.apply(calc_VT_VP, args=(vt_vp['vpth2'],), axis=1)
    dfw['THITH2'] = dfw[get_THITH2_columns(dfw.columns)].apply(calc_THITH2, axis = 1)

    dfw['THILT1_PRINT'] = dfw[['VTLT1', 'VPLT1', 'THILT1']].apply(calc_THILT1_PRINT, axis = 1)
    dfw['THITH1_PRINT'] = dfw[['VTTH1', 'VPTH1', 'THITH1']].apply(calc_THITH1_PRINT, axis = 1)
    dfw['TB1'] = dfw[get_TB1_columns(dfw.columns)].apply(calc_TB1, axis=1)
    dfw['NOTE1'] = dfw[get_NOTE1_columns(dfw.columns)].apply(calc_NOTE1, axis=1)

    dfw['THILT2_PRINT'] = dfw[['VTLT2', 'VPLT2', 'THILT1', 'THILT2']].apply(calc_THILT2_PRINT, axis = 1)
    dfw['THITH2_PRINT'] = dfw[['VTTH2', 'VPTH2', 'THITH1', 'THITH2']].apply(calc_THITH2_PRINT, axis = 1)
    dfw['TB2'] = dfw[get_TB2_columns(dfw.columns)].apply(calc_TB2, axis=1)
    dfw['NOTE2'] = dfw[get_NOTE2_columns(dfw.columns)].apply(calc_NOTE2, axis=1)

    return dfw

