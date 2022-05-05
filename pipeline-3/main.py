import const
import write_helper as wh
import read_helper as rh

def INFO1001_2021_YRD_1_RHM_2021_LAN1():
    obj = const.INFO1001_2021_YRD_1_RHM_2021_LAN1
    data = rh.read_data(obj['input'], obj['lan_thi'])
    # print(df.tail(10))
    wh.write_bang_diem_psc_export_INFO1001(
        df=data[0], summary=data[1], path=obj['output'], 
        footer='INFO1001-2021-YRD-1',
        mon='Thống kê y học [2 TC]', lop='RHM-2021', 
        lop_hp='211TKY_01001203', lan_thi=obj['lan_thi'],
        ngay_thi='14/04/2022',
        ngay='      ', thang='05', nam='2022'
    )

def INFO1001_2021_YRD_1_DUOC_2021_LAN1():
    obj = const.INFO1001_2021_YRD_1_DUOC_2021_LAN1
    data = rh.read_data(obj['input'], obj['lan_thi'])
    wh.write_bang_diem_psc_export_INFO1001(
        df=data[0], summary=data[1], path=obj['output'],
        footer='INFO1001-2021-YRD-1',
        mon='Thống kê y học [2 TC]', lop='DUOC-2021', 
        lop_hp='211TKY_01001201', lan_thi=obj['lan_thi'],
        ngay_thi='14/04/2022',
        ngay='      ', thang='05', nam='2022'
    )

def INFO1001_2021_YRD_1_Y_2021_LAN1():
    obj = const.INFO1001_2021_YRD_1_Y_2021_LAN1
    data = rh.read_data(obj['input'], obj['lan_thi'])
    wh.write_bang_diem_psc_export_INFO1001(
        df=data[0], summary=data[1], path=obj['output'],
        footer='INFO1001-2021-YRD-1',
        mon='Thống kê y học [2 TC]', lop='Y-2021', 
        lop_hp='211TKY_01001203', lan_thi=obj['lan_thi'],
        ngay_thi='14/04/2022',
        ngay='      ', thang='05', nam='2022'
    )

def INFO1001_2021_YRD_1_HL_1_LAN1():
    obj = const.INFO1001_2021_YRD_1_HL_1_LAN1
    data = rh.read_data(obj['input'], obj['lan_thi'])
    wh.write_bang_diem_psc_export_INFO1001(
        df=data[0], summary=data[1], path=obj['output'],
        footer='INFO1001-2021-YRD-1',
        mon='Thống kê y học [2 TC]', lop='HL-1', 
        lop_hp='', lan_thi=obj['lan_thi'],
        ngay_thi='14/04/2022',
        ngay='      ', thang='05', nam='2022'
    )

def INFO1001_2020_YRD_1_RHM_2020_LAN2():
    obj = const.INFO1001_2020_YRD_1_RHM_2020_LAN2
    data = rh.read_data(obj['input'], obj['lan_thi'])
    wh.write_bang_diem_psc_export_INFO1001(
        df=data[0], summary=data[1], path=obj['output'],
        footer='INFO1001-2020-YRD-1',
        mon='Thống kê y học [2 TC]', lop='RHM-2020', 
        lop_hp='', lan_thi=obj['lan_thi'],
        ngay_thi='14/04/2022',
        ngay='      ', thang='05', nam='2022'
    )



def main():
    INFO1001_2021_YRD_1_RHM_2021_LAN1()
    INFO1001_2021_YRD_1_DUOC_2021_LAN1()
    INFO1001_2021_YRD_1_Y_2021_LAN1()
    INFO1001_2021_YRD_1_HL_1_LAN1()
    INFO1001_2020_YRD_1_RHM_2020_LAN2()

if __name__ == '__main__':
    main()