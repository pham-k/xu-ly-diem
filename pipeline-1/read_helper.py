import pandas as pd

import core

def read_response(fp, course_id):
    df = pd.read_parquet(fp).query(f'course_id == "{course_id}"')
    return df

def read_attendee(fp, skiprows=9, usecols=[1, 2, 3, 5]):
    df= pd.read_excel(
        fp,
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
    )
    return df[['user_id', 'name_last', 'name_first', 'note']]

