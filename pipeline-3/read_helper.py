import pandas as pd

def read_data(fp, lan_thi='1'):
    """
    Read xls file psc-export-[filename].xls

    Args:
        fp: file path
        lan_thi: int, lan thi

    Return:
        df: A dataframe
    """
    dtype = {
        'Mã HV': 'str',
        'Họ': 'str',
        'Tên': 'str',
        'CC': 'float',
        'GHP': 'float',
        'Thi_LT': 'str',
        'Thi_TH': 'str',
        'Điểm HP': 'str',
        'Ghi chú': 'str'
    }
    cols = {
        'Mã HV': 'user_id',
        'Họ': 'name_last',
        'Tên': 'name_first',
        'CC': 'CC',
        'GHP': 'QT',
        'Thi_LT': f'THILT{lan_thi}_PRINT',
        'Thi_TH': f'THITH{lan_thi}_PRINT',
        'Điểm HP': f'TB{lan_thi}',
        'Ghi chú': f'NOTE{lan_thi}'
    }
    df = pd.read_excel(
        fp, skiprows = 9, 
        usecols = [*dtype], dtype=dtype
    ).rename(columns=cols)
    df = df.loc[df['user_id'].notna()].fillna('')
    return df
