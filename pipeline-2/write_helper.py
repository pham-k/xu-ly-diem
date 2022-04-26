import pandas as pd
import numpy as np
from pathlib import Path
import re
import xlsxwriter
import mark_helper as mh

def write_mau_import_diem_INFO1001(
    df, path,
    mon='', lop='', lop_hp='', lan_thi=''):

    workbook = xlsxwriter.Workbook(path)
    worksheet = workbook.add_worksheet()
    worksheet.set_portrait()
    worksheet.set_paper(9)  # A4
    worksheet.center_horizontally()
    worksheet.set_margins(left=1, right=1, top=1, bottom=1)
    worksheet.repeat_rows(9)
    # worksheet.set_print_scale()
    worksheet.set_column(0, 0, 4)
    worksheet.set_column(1, 1, 12)
    worksheet.set_column(2, 2, 32)
    worksheet.set_column(3, 3, 12)
    worksheet.set_column(4, 7, 8)  # Them diem thi TH
    worksheet.set_column(8, 8, 12)
    align_center = workbook.add_format({'align': 'center'})
    bold = workbook.add_format({'bold': True})
    header_format = workbook.add_format({'align': 'center', 'bold': True, 'border': 1})
    mark_format = workbook.add_format({'num_format': '0.0', 'border': 1, 'align': 'right'})
    cell_format_center = workbook.add_format({'border': 1, 'align': 'center'})
    cell_format_left = workbook.add_format({'border': 1, 'align': 'left'})

    # Metadata
    worksheet.merge_range(
        'A1:I1',
        'TRƯỜNG ĐẠI HỌC Y KHOA PHẠM NGỌC THẠCH',
        workbook.add_format({'align': 'center'}))

    worksheet.merge_range(
        'A2:I2',
        'ỦY BAN NHÂN DÂN THÀNH PHỐ HỒ CHÍ MINH',
        workbook.add_format({'align': 'center', 'bold': True}))

    worksheet.merge_range(
        'A3:I3',
        '-------------------',
        workbook.add_format({'align': 'center', 'bold': True}))

    worksheet.merge_range(
        'A4:I4',
        'MẪU IMPORT ĐIỂM',
        workbook.add_format({'align': 'center', 'bold': True}))

    worksheet.merge_range(
        'A5:I5',
        'MÔN HỌC: ' + mon,
        workbook.add_format({'align': 'center', 'bold': True}))

    worksheet.merge_range(
        'A6:I6',
        'MÃ LỚP HỌC PHẦN: ' + lop_hp,
        workbook.add_format({'align': 'center', 'bold': True}))

    worksheet.merge_range(
        'A7:I7',
        'MÃ LỚP: ' + lop,
        workbook.add_format({'align': 'center', 'bold': True}))

    worksheet.merge_range(
        'A8:I8',
        'LẦN THI: ' + lan_thi,
        workbook.add_format({'align': 'center', 'bold': True}))

    # Header
    worksheet.write(
        'A10',
        'STT',
        header_format)

    worksheet.write(
        'B10',
        'MSSV',
        header_format)

    worksheet.merge_range(
        'C10:D10',
        'Họ và tên',
        header_format)

    worksheet.write(
        'E10',
        'CC',
        header_format)

    worksheet.write(
        'F10',
        'GHP',
        header_format)

    worksheet.write(
        'G10',
        'Thi#LT',
        header_format)
    
    worksheet.write(
        'H10',
        'Thi#TH',
        header_format)

    worksheet.write(
        'I10',
        'NOTE',
        header_format)

    # write data
    worksheet.write_column('A11', df.index + 1, cell_format_center)
    worksheet.write_column('B11', df['user_id'], cell_format_center)
    worksheet.write_column('C11', df['name_last'], cell_format_left)
    worksheet.write_column('D11', df['name_first'], cell_format_left)
    worksheet.write_column('E11', df['CC'], mark_format)
    worksheet.write_column('F11', df['QT'], mark_format)
    worksheet.write_column('G11', df[f'THILT{lan_thi}_PRINT'], mark_format)
    worksheet.write_column('H11', df[f'THITH{lan_thi}_PRINT'], mark_format)
    worksheet.write_column('I11', df['note'].fillna(''), cell_format_left)
    workbook.close()
    
    
def write_bang_diem_INFO1001(df, path, footer='',
                         mon='', lop='', lop_hp='', lan_thi='', ngay_thi='',
                         ngay='      ', thang='03', nam='2022'):
    table_row = df.shape[0]
    workbook = xlsxwriter.Workbook(path)
    worksheet = workbook.add_worksheet()
    worksheet.set_portrait()
    worksheet.set_paper(9)  # A4
    worksheet.center_horizontally()
    worksheet.set_margins(left=0.7, right=0.7, top=0.75, bottom=0.75)
    worksheet.repeat_rows(10)
    worksheet.print_area(0, 0, 10 + table_row + 21, 9)
    worksheet.set_print_scale(75)
    worksheet.set_footer(f'&C&P/&N&R{footer}')
    worksheet.set_column(0, 0, 4)
    worksheet.set_column(1, 1, 12)
    worksheet.set_column(2, 2, 28)
    worksheet.set_column(3, 3, 12)
    worksheet.set_column(4, 8, 8)
    worksheet.set_column(9, 9, 14)
    worksheet.set_row(3, 8)
    align_center = workbook.add_format({'align': 'center'})
    bold = workbook.add_format({'bold': True})
    header_format = workbook.add_format({'align': 'center', 'bold': True, 'border': 1})
    mark_format = workbook.add_format({'num_format': '0.0', 'border': 1, 'align': 'right'})
    cell_format_center = workbook.add_format({'border': 1, 'align': 'center'})
    cell_format_left = workbook.add_format({'border': 1, 'align': 'left'})

    # Metadata
    worksheet.merge_range(
        'A1:J1',
        'TRƯỜNG ĐẠI HỌC Y KHOA PHẠM NGỌC THẠCH',
        workbook.add_format({'align': 'center'}))

    worksheet.merge_range(
        'A2:J2',
        'KHOA Y TẾ CÔNG CỘNG',
        workbook.add_format({'align': 'center'}))
    
    worksheet.merge_range(
        'A3:J3',
        'BỘ MÔN TIN HỌC - THỐNG KÊ Y HỌC',
        workbook.add_format({'align': 'center', 'bold': True}))

    worksheet.merge_range(
        'A4:J4',
        '\u23AF' * 8,
        workbook.add_format({'align': 'center', 'bold': True}))

    worksheet.merge_range(
        'A5:J5',
        'BẢNG ĐIỂM',
        workbook.add_format({'align': 'center', 'bold': True}))

    worksheet.merge_range(
        'A6:J6',
        'MÔN HỌC: ' + mon,
        workbook.add_format({'align': 'center', 'bold': True}))

    worksheet.merge_range(
        'A7:J7',
        'MÃ LỚP HỌC PHẦN: ' + lop_hp,
        workbook.add_format({'align': 'center', 'bold': True}))

    worksheet.merge_range(
        'A8:J8',
        'MÃ LỚP: ' + lop,
        workbook.add_format({'align': 'center', 'bold': True}))

    worksheet.merge_range(
        'A9:J9',
        'LẦN THI: ' + lan_thi,
        workbook.add_format({'align': 'center', 'bold': True}))

    worksheet.write(
        'A10',
        'Ngày thi: ' + ngay_thi,
        workbook.add_format({'align': 'left', 'italic': True}))
    
    # Header
    worksheet.write(
        'A11',
        'STT',
        header_format)

    worksheet.write(
        'B11',
        'MSSV',
        header_format)

    worksheet.merge_range(
        'C11:D11',
        'Họ và tên',
        header_format)

    worksheet.write(
        'E11',
        'CC',
        header_format)

    worksheet.write(
        'F11',
        'GHP',
        header_format)

    worksheet.write(
        'G11',
        'Thi#LT',
        header_format)
    
    worksheet.write(
        'H11',
        'Thi#TH',
        header_format)
    
    worksheet.write(
        'I11',
        'TB',
        header_format)

    worksheet.write(
        'J11',
        'Ghi chú',
        header_format)

    # write data
    worksheet.write_column('A12', df.index + 1, cell_format_center)
    worksheet.write_column('B12', df['user_id'], cell_format_center)
    worksheet.write_column('C12', df['name_last'], cell_format_left)
    worksheet.write_column('D12', df['name_first'], cell_format_left)
    worksheet.write_column('E12', df['CC'], mark_format)
    worksheet.write_column('F12', df['QT'], mark_format)
    worksheet.write_column('G12', df[f'THILT{lan_thi}_PRINT'], mark_format)
    worksheet.write_column('H12', df[f'THITH{lan_thi}_PRINT'], mark_format)
    worksheet.write_column('I12', df[f'TB{lan_thi}'], mark_format)
    worksheet.write_column('J12', df[f'NOTE{lan_thi}'].fillna(''), cell_format_left)
    
    # Tinh tong, du thi, dau, rot, vang
    tong_so = table_row
    vang = df[(df[f'VTLT{lan_thi}'] == True) | (df[f'VTTH{lan_thi}'] == True)].shape[0]
    du_thi = tong_so - vang
    try:
        rot_lt = df[f'NOTE{lan_thi}'].value_counts(dropna=False)['Rớt LT']
    except:
        rot_lt = 0
    try:
        rot_th = df[f'NOTE{lan_thi}'].value_counts(dropna=False)['Rớt TH']
    except:
        rot_th = 0
    try:
        rot_lt_th = df[f'NOTE{lan_thi}'].value_counts(dropna=False)['Rớt LT, TH']
    except:
        rot_lt_th = 0
    try:
        rot_tb = df[f'NOTE{lan_thi}'].value_counts(dropna=False)['Rớt']
    except:
        rot_tb = 0
    try:
        dau = df[f'NOTE{lan_thi}'].value_counts(dropna=False)['']
    except:
        dau = 0
    # print(df[f'NOTE{lan_thi}'].value_counts(dropna=False))
    rot = rot_lt + rot_th + rot_lt_th + rot_tb
    
    # write data
    worksheet.write(
        f'B{10 + df.shape[0] + 3}', 
        f'Tổng số: ',
        workbook.add_format({'align': 'right', 'italic': True}))
    worksheet.write(
        f'C{10 + table_row + 3}', 
        tong_so,
        workbook.add_format({'align': 'left', 'italic': True}))
    worksheet.write(
        f'B{10 + table_row + 4}', 
        f'Dự thi: ',
        workbook.add_format({'align': 'right', 'italic': True}))
    worksheet.write(
        f'C{10 + table_row + 4}', 
        du_thi,
        workbook.add_format({'align': 'left', 'italic': True}))
    worksheet.write(
        f'B{10 + table_row + 5}', 
        f'Đậu: ',
        workbook.add_format({'align': 'right', 'italic': True}))
    worksheet.write(
        f'C{10 + table_row + 5}', 
        dau,
        workbook.add_format({'align': 'left', 'italic': True}))
    worksheet.write(
        f'B{10 + table_row + 6}', 
        f'Rớt: ',
        workbook.add_format({'align': 'right', 'italic': True}))
    worksheet.write(
        f'C{10 + table_row + 6}', 
        rot,
        workbook.add_format({'align': 'left', 'italic': True}))
    worksheet.write(
        f'B{10 + table_row + 7}', 
        f'Vắng: ',
        workbook.add_format({'align': 'right', 'italic': True}))
    worksheet.write(
        f'C{10 + table_row + 7}', 
        vang,
        workbook.add_format({'align': 'left', 'italic': True}))
    
    worksheet.merge_range(
        f'E{10 + table_row + 8}:J{10 + table_row + 8}',
        f'Tp. Hồ Chí Minh, ngày {ngay} tháng {thang} năm {nam}',
        workbook.add_format({'align': 'center', 'italic': True}))
    
    worksheet.merge_range(
        f'A{10 + table_row + 9}:D{10 + table_row + 9}',
        'GIÁO VỤ BỘ MÔN',
        workbook.add_format({'align': 'center', 'bold': True}))
    
    worksheet.merge_range(
        f'A{10 + table_row + 14}:D{10 + table_row + 14}',
        'BS. Phạm Hoàng Gia Khương',
        workbook.add_format({'align': 'center', 'bold': True}))
    
    worksheet.merge_range(
        f'E{10 + table_row + 9}:J{10 + table_row + 9}',
        'TRƯỞNG BỘ MÔN',
        workbook.add_format({'align': 'center', 'bold': True}))
    
    worksheet.merge_range(
        f'E{10 + table_row + 14}:J{10 + table_row + 14}',
        'TS. BS. Nguyễn Ngọc Vân Phương',
        workbook.add_format({'align': 'center', 'bold': True}))
    
    worksheet.merge_range(
        f'A{10 + table_row + 17}:D{10 + table_row + 17}',
        'PHÒNG QUẢN LÝ ĐÀO TẠO ĐẠI HỌC',
        workbook.add_format({'align': 'center', 'bold': True}))
    
    workbook.close()
