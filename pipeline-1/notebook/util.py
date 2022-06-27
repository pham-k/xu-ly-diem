import pandas as pd
import numpy as np
from pathlib import Path
import re
import xlsxwriter


def round_half_up(n, decimals=0):
    multiplier = 10 ** decimals
    # Replace math.floor with np.floor
    return np.floor(n*multiplier + 0.5) / multiplier


def parse_response(path, regex_user_id='(.*?)\.', regex_year='(.*?)\.'):
    DTYPE = {
        'Score': 'float',
        'MSSV': 'string',
        'HỌ TÊN': 'string',
        'LỚP': 'string',
        'NIÊN KHÓA': 'string'
    }
    COLNAME = ['score', 'user_id', 'name', 'class_name', 'year']
    CLASS_LABEL = {
        'DIEUDUONG': 'DD',
        'DINHDUONG': 'DHD',
        'KXNK': 'KX',
        'KTYH': 'KT',
        'YTCC': 'YT',
        'XNYH': 'XN',
        'YA': 'YA',
        'YB': 'YB',
        'YC': 'YC',
        'YD': 'YD',
        'RHM': 'RHM',
        'DUOC': 'DUOC',
        'YVD': 'YVD',
        'HS': 'DD',
        'PHCN': 'DD',
        'GMHS': 'DD'
    }
    df = pd.read_excel(
        path,
        usecols=DTYPE.keys(),
        dtype=DTYPE)
    df.columns = COLNAME
    
    if regex_user_id:
        df['user_id'] = df['user_id'].str.extract(regex_user_id)
    
    df['name'] = df['name'].str.upper()
    df['class_1'] = df['class_name'].replace(CLASS_LABEL)
    if regex_year:
        df['year_1'] = df['year'].str.extract('(.*?)\.')
    else:
        df['year_1'] = df['year']

    df['class_id'] = [str(x) + '-' + y for x, y in zip(df['class_1'], df['year_1'])]
    try:
        df.loc[df['class_id'].str.startswith('KHAC'), 'class_id'] = ''
    except:
        pass
    
    return df[['score', 'user_id', 'class_id', 'name']]


def get_attendee(input_path, course_id='course_id', class_id="class_id", skiprows=9, usecols=[1, 2, 3]):
    df= pd.read_excel(
        input_path,
        index_col=None,
        skiprows=skiprows,
        usecols=usecols,
        dtype={'MSSV': 'string'}
    )
    df.rename(
        columns={
            df.columns[0]: 'user_id',
            df.columns[1]: 'name_last',
            df.columns[2]: 'name_first',
        },
        inplace=True
    )
    df['user_id'] = df['user_id'].astype('str')
    df = df.assign(
        name_first = df.name_first.str.strip().str.upper(),
        name_last = df.name_last.str.strip().str.upper(),
        course_id = course_id,
        class_id = class_id,
    )
#     df = df.set_index(['user_id', 'class_id', 'course_id'])
    return df[['user_id', 'class_id', 'course_id', 'name_last', 'name_first']]


def get_examinee(attendee, mark_long, exam, how='left'):
    
    attendee = attendee[['user_id', 'name_last', 'name_first', 'note']]
    df = attendee.merge(mark_long, how=how, indicator=True,
                       left_on='user_id', right_on='user_id')
    # df['is_absent'] = df.mark.isna()
    # df['is_absent_with_permission'] = False
    # df.rename(columns={
    #     'class_id_x': 'class_id_from_attendee',
    #     'class_id_y': 'class_id_from_response',
    # }, inplace=True)
    df1 = df.merge(exam, left_on='exam_id', right_on='exam_id')
    return df1[[
        'user_id',
        'class_id',
        # 'class_id_from_attendee', 'class_id_from_response',
        'course_id', 'exam_id',
        'exam_category',
        'name_last', 'name_first', 'mark', 
        # 'is_absent', 'is_absent_with_permission',
        'note', '_merge']]
    # return df1
    

def get_attendee(input_path, course_id='course_id', skiprows=9, usecols=[1, 2, 3, 5]):
    df= pd.read_excel(
        input_path,
        index_col=None,
        skiprows=skiprows,
        usecols=usecols,
        dtype={'MSSV': 'string'}
    )
    df.rename(
        columns={
            df.columns[0]: 'user_id',
            df.columns[1]: 'name_last',
            df.columns[2]: 'name_first',
            df.columns[3]: 'note',
        },
        inplace=True
    )
    df['user_id'] = df['user_id'].astype('str')
    df = df.assign(
        name_first = df.name_first.str.strip().str.upper(),
        name_last = df.name_last.str.strip().str.upper(),
        course_id = course_id,
        # class_id = class_id,
    )
#     df = df.set_index(['user_id', 'class_id', 'course_id'])
    return df[['user_id', 'course_id', 'name_last', 'name_first', 'note']]


def parse_exam(path, dtype={'id': 'string', 'category': 'string'}, 
               colname={'id': 'exam_id', 'category': 'exam_category'}):
    df = pd.read_excel(
        path,
        usecols=dtype.keys(),
        dtype=dtype)
    df.rename(columns=colname, inplace=True)
    return df[['exam_id', 'exam_category']]




