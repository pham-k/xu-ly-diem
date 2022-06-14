import read_helper as rh
import mark_helper as mh
import write_helper as wh
import const

def write_STAT1001_2021_KX_2_KX_2021_LAN1():
    response = rh.read_response(const.PATH_RESPONSE, course_id='STAT1001-2021-KX-2')
    attendee = rh.read_attendee(const.PATH_ATTENDEE_KX_2020_LAN1)
    df = mh.calc(
        attendee=attendee, response=response,
        course_id='STAT1001-2021-KX-2',
        vt_vp={
            'vt1': const.VT_KX_2020_LAN1, 'vp1': const.VP_KX_2020_LAN1,
            'vt2': const.VT_KX_2020_LAN2, 'vp2': const.VP_KX_2020_LAN2,
        })
    # df.to_excel('foo.xlsx')
    # show_cols = [0] + list(range(8,16))
    # print(df.info())
    # print(df.iloc[:, show_cols].sample(5))
    # print(df[df['STAT1001-2021-KX-2-THI1'].isna()])
    # print(df.query('user_id == "2056990004"').iloc[:, show_cols])

    wh.write_mau_import_diem_STAT1001(
        df,
        path=const.PATH_MAU_IMPORT_DIEM_KX_2020_LAN1,
        mon='Thống kê y học [2 TC]',
        lop='KX-2020',
        lop_hp='211XTK_01081001',
        lan_thi='1',
    )

    wh.write_bang_diem_STAT1001(
        df,
        path=const.PATH_BANG_DIEM_KX_2020_LAN1,
        mon='Thống kê y học [2 TC]',
        lop='KX-2020',
        lop_hp='211XTK_01081001',
        ngay_thi='08/03/2022',
        ngay='      ',
        thang='      ',
        nam='2022',
        footer='STAT1001-2021-KX-2',
        lan_thi='1',
    )

def write_STAT1001_2021_KX_2_DD_2018_LAN1():
    response = rh.read_response(const.PATH_RESPONSE, course_id='STAT1001-2021-KX-2')
    attendee = rh.read_attendee(const.PATH_ATTENDEE_DD_2018_LAN1)
    df = mh.calc(
        attendee=attendee, response=response,
        course_id='STAT1001-2021-KX-2',
        vt_vp={
            'vt1': const.VT_DD_2018_LAN1, 'vp1': const.VP_DD_2018_LAN1,
            'vt2': const.VT_DD_2018_LAN2, 'vp2': const.VP_DD_2018_LAN2,
        })

    wh.write_mau_import_diem_STAT1001(
        df,
        path=const.PATH_MAU_IMPORT_DIEM_DD_2018_LAN1,
        mon='Xác suất – Thống kê y học [2 TC]',
        lop='DD-2018',
        lop_hp='211TKY01991001',
        lan_thi='1',
    )

    wh.write_bang_diem_STAT1001(
        df,
        path=const.PATH_BANG_DIEM_DD_2018_LAN1,
        mon='Xác suất – Thống kê y học [2 TC]',
        lop='DD-2018',
        lop_hp='211TKY01991001',
        ngay_thi='08/03/2022',
        ngay='      ',
        thang='      ',
        nam='2022',
        footer='STAT1001-2021-KX-2',
        lan_thi='1',
    )

def write_STAT1001_2021_KX_2_KX_2021_LAN2():
    response = rh.read_response(const.PATH_RESPONSE, course_id='STAT1001-2021-KX-2')
    attendee = rh.read_attendee(const.PATH_ATTENDEE_KX_2020_LAN2)
    df = mh.calc(
        attendee=attendee, response=response,
        course_id='STAT1001-2021-KX-2',
        vt_vp={
            'vt1': const.VT_KX_2020_LAN1, 'vp1': const.VP_KX_2020_LAN1,
            'vt2': const.VT_KX_2020_LAN2, 'vp2': const.VP_KX_2020_LAN2,
        })
    # df.to_excel('foo.xlsx')
    # show_cols = [0] + list(range(8,16))
    # print(df.info())
    # print(df.iloc[:, show_cols].sample(5))
    # print(df[df['STAT1001-2021-KX-2-THI1'].isna()])
    # print(df.query('user_id == "2056990004"').iloc[:, show_cols])

    wh.write_mau_import_diem_STAT1001(
        df,
        path=const.PATH_MAU_IMPORT_DIEM_KX_2020_LAN2,
        mon='Thống kê y học [2 TC]',
        lop='KX-2020',
        lop_hp='211XTK_01081001',
        lan_thi='2',
    )

    wh.write_bang_diem_STAT1001(
        df,
        path=const.PATH_BANG_DIEM_KX_2020_LAN2,
        mon='Thống kê y học [2 TC]',
        lop='KX-2020',
        lop_hp='211XTK_01081001',
        ngay_thi='23/03/2022',
        ngay='      ',
        thang='      ',
        nam='2022',
        footer='STAT1001-2021-KX-2',
        lan_thi='2',
    )

def write_STAT1001_2021_KX_2_DD_2018_LAN2():
    response = rh.read_response(const.PATH_RESPONSE, course_id='STAT1001-2021-KX-2')
    attendee = rh.read_attendee(const.PATH_ATTENDEE_DD_2018_LAN2)
    df = mh.calc(
        attendee=attendee, response=response,
        course_id='STAT1001-2021-KX-2',
        vt_vp={
            'vt1': const.VT_DD_2018_LAN1, 'vp1': const.VP_DD_2018_LAN1,
            'vt2': const.VT_DD_2018_LAN2, 'vp2': const.VP_DD_2018_LAN2,
        })
    # df.to_excel('foo.xlsx')
    wh.write_mau_import_diem_STAT1001(
        df,
        path=const.PATH_MAU_IMPORT_DIEM_DD_2018_LAN2,
        mon='Xác suất – Thống kê y học [2 TC]',
        lop='DD-2018',
        lop_hp='211TKY01991001',
        lan_thi='2',
    )

    wh.write_bang_diem_STAT1001(
        df,
        path=const.PATH_BANG_DIEM_DD_2018_LAN2,
        mon='Xác suất – Thống kê y học [2 TC]',
        lop='DD-2018',
        lop_hp='211TKY01991001',
        ngay_thi='23/03/2022',
        ngay='      ',
        thang='      ',
        nam='2022',
        footer='STAT1001-2021-KX-2',
        lan_thi='2',
    )

def write_STAT1002_2021_YRD_1_Y_2021_LAN1():
    response = rh.read_response(const.PATH_RESPONSE, course_id='STAT1002-2021-YRD-1')
    attendee = rh.read_attendee(const.PATH_ATTENDEE_Y_2021_LAN1)
    df = mh.calc(
        attendee=attendee, response=response,
        course_id='STAT1002-2021-YRD-1',
        vt_vp={
            'vt1': const.VT_Y_2021_LAN1, 'vp1': const.VP_Y_2021_LAN1,
            'vt2': const.VT_Y_2021_LAN2, 'vp2': const.VP_Y_2021_LAN2,
        })
    # df.to_excel('foo.xlsx')

    wh.write_mau_import_diem_STAT1001(
        df,
        path=const.PATH_MAU_IMPORT_DIEM_Y_2021_LAN1,
        mon='Thống kê y học [2 TC]',
        lop='Y-2021',
        lop_hp='211TKY_01001203'
    )

    wh.write_bang_diem_STAT1001(
        df,
        path=const.PATH_BANG_DIEM_Y_2021_LAN1,
        mon='Thống kê y học [2 TC]',
        lop='Y-2021',
        lop_hp='211TKY_01001203',
        ngay_thi='21/04/2022',
        ngay='      ',
        thang='      ',
        nam='2022',
        footer='STAT1002-2021-YRD-1'
    )

def write_STAT1002_2021_YRD_1_RHM_2021_LAN1():
    response = rh.read_response(const.PATH_RESPONSE, course_id='STAT1002-2021-YRD-1')
    attendee = rh.read_attendee(const.PATH_ATTENDEE_RHM_2021_LAN1)
    df = mh.calc(
        attendee=attendee, response=response,
        course_id='STAT1002-2021-YRD-1',
        vt_vp={
            'vt1': const.VT_RHM_2021_LAN1, 'vp1': const.VP_RHM_2021_LAN1,
            'vt2': const.VT_RHM_2021_LAN2, 'vp2': const.VP_RHM_2021_LAN2,
        })
    # df.to_excel('foo.xlsx')

    wh.write_mau_import_diem_STAT1001(
        df,
        path=const.PATH_MAU_IMPORT_DIEM_RHM_2021_LAN1,
        mon='Thống kê y học [2 TC]',
        lop='RHM-2021',
        lop_hp='211TKY_01001205'
    )

    wh.write_bang_diem_STAT1001(
        df,
        path=const.PATH_BANG_DIEM_RHM_2021_LAN1,
        mon='Thống kê y học [2 TC]',
        lop='RHM-2021',
        lop_hp='211TKY_01001205',
        ngay_thi='21/04/2022',
        ngay='      ',
        thang='      ',
        nam='2022',
        footer='STAT1002-2021-YRD-1'
    )

def write_STAT1002_2021_YRD_1_DUOC_2021_LAN1():
    response = rh.read_response(const.PATH_RESPONSE, course_id='STAT1002-2021-YRD-1')
    attendee = rh.read_attendee(const.PATH_ATTENDEE_DUOC_2021_LAN1)
    df = mh.calc(
        attendee=attendee, response=response,
        course_id='STAT1002-2021-YRD-1',
        vt_vp={
            'vt1': const.VT_DUOC_2021_LAN1, 'vp1': const.VP_DUOC_2021_LAN1,
            'vt2': const.VT_DUOC_2021_LAN2, 'vp2': const.VP_DUOC_2021_LAN2,
        })
    # df.to_excel('foo.xlsx')

    wh.write_mau_import_diem_STAT1001(
        df,
        path=const.PATH_MAU_IMPORT_DIEM_DUOC_2021_LAN1,
        mon='Thống kê y học [2 TC]',
        lop='DUOC-2021',
        lop_hp='211TKY_01001201'
    )

    wh.write_bang_diem_STAT1001(
        df,
        path=const.PATH_BANG_DIEM_DUOC_2021_LAN1,
        mon='Thống kê y học [2 TC]',
        lop='DUOC-2021',
        lop_hp='211TKY_01001201',
        ngay_thi='21/04/2022',
        ngay='      ',
        thang='      ',
        nam='2022',
        footer='STAT1002-2021-YRD-1'
    )

def write_STAT1002_2021_YRD_1_HL_1_LAN1():
    response = rh.read_response(const.PATH_RESPONSE, course_id='STAT1002-2021-YRD-1')
    attendee = rh.read_attendee(const.PATH_ATTENDEE_HL_1_LAN1)
    df = mh.calc(
        attendee=attendee, response=response,
        course_id='STAT1002-2021-YRD-1',
        vt_vp={
            'vt1': const.VT_HL_1_LAN1, 'vp1': const.VP_HL_1_LAN1,
            'vt2': const.VT_HL_1_LAN2, 'vp2': const.VP_HL_1_LAN2,
        })
    # df.to_excel('foo.xlsx')

    wh.write_mau_import_diem_STAT1001(
        df,
        path=const.PATH_MAU_IMPORT_DIEM_HL_1_LAN1,
        mon='Thống kê y học [2 TC]',
        lop='HL-1',
        lop_hp='211TKY_01001207'
    )

    wh.write_bang_diem_STAT1001(
        df,
        path=const.PATH_BANG_DIEM_HL_1_LAN1,
        mon='Thống kê y học [2 TC]',
        lop='HL-1',
        lop_hp='211TKY_01001207',
        ngay_thi='21/04/2022',
        ngay='      ',
        thang='      ',
        nam='2022',
        footer='STAT1002-2021-YRD-1'
    )

def write_STAT1002_2021_YRD_1_Y_2021_LAN2():
    response = rh.read_response(const.PATH_RESPONSE, course_id='STAT1002-2021-YRD-1')
    attendee = rh.read_attendee(const.PATH_ATTENDEE_Y_2021_LAN2)
    df = mh.calc(
        attendee=attendee, response=response,
        course_id='STAT1002-2021-YRD-1',
        vt_vp={
            'vt1': const.VT_Y_2021_LAN1, 'vp1': const.VP_Y_2021_LAN1,
            'vt2': const.VT_Y_2021_LAN2, 'vp2': const.VP_Y_2021_LAN2,
        })
    # df.to_excel('foo.xlsx')

    wh.write_mau_import_diem_STAT1001(
        df,
        path=const.PATH_MAU_IMPORT_DIEM_Y_2021_LAN2,
        mon='Thống kê y học [2 TC]',
        lop='Y-2021',
        lop_hp='211TKY_01001203',
        lan_thi='2'
    )

    wh.write_bang_diem_STAT1001(
        df,
        path=const.PATH_BANG_DIEM_Y_2021_LAN2,
        mon='Thống kê y học [2 TC]',
        lop='Y-2021',
        lop_hp='211TKY_01001203',
        ngay_thi='07/05/2022',
        ngay='      ',
        thang='      ',
        nam='2022',
        footer='STAT1002-2021-YRD-1',
        lan_thi='2'
    )

def write_STAT1002_2021_YRD_1_RHM_2021_LAN2():
    response = rh.read_response(const.PATH_RESPONSE, course_id='STAT1002-2021-YRD-1')
    attendee = rh.read_attendee(const.PATH_ATTENDEE_RHM_2021_LAN2)
    df = mh.calc(
        attendee=attendee, response=response,
        course_id='STAT1002-2021-YRD-1',
        vt_vp={
            'vt1': const.VT_RHM_2021_LAN1, 'vp1': const.VP_RHM_2021_LAN1,
            'vt2': const.VT_RHM_2021_LAN2, 'vp2': const.VP_RHM_2021_LAN2,
        })
    # df.to_excel('foo.xlsx')

    wh.write_mau_import_diem_STAT1001(
        df,
        path=const.PATH_MAU_IMPORT_DIEM_RHM_2021_LAN2,
        mon='Thống kê y học [2 TC]',
        lop='RHM-2021',
        lop_hp='211TKY_01001205',
        lan_thi='2'
    )

    wh.write_bang_diem_STAT1001(
        df,
        path=const.PATH_BANG_DIEM_RHM_2021_LAN2,
        mon='Thống kê y học [2 TC]',
        lop='RHM-2021',
        lop_hp='211TKY_01001205',
        ngay_thi='07/05/2022',
        ngay='      ',
        thang='      ',
        nam='2022',
        footer='STAT1002-2021-YRD-1',
        lan_thi='2'
    )

def write_STAT1002_2021_YRD_1_HL_1_LAN2():
    response = rh.read_response(const.PATH_RESPONSE, course_id='STAT1002-2021-YRD-1')
    attendee = rh.read_attendee(const.PATH_ATTENDEE_HL_1_LAN2)
    df = mh.calc(
        attendee=attendee, response=response,
        course_id='STAT1002-2021-YRD-1',
        vt_vp={
            'vt1': const.VT_HL_1_LAN1, 'vp1': const.VP_HL_1_LAN1,
            'vt2': const.VT_HL_1_LAN2, 'vp2': const.VP_HL_1_LAN2,
        })
    # df.to_excel('foo.xlsx')

    wh.write_mau_import_diem_STAT1001(
        df,
        path=const.PATH_MAU_IMPORT_DIEM_HL_1_LAN2,
        mon='Thống kê y học [2 TC]',
        lop='HL-1',
        lop_hp='211TKY_01001207',
        lan_thi='2'
    )

    wh.write_bang_diem_STAT1001(
        df,
        path=const.PATH_BANG_DIEM_HL_1_LAN2,
        mon='Thống kê y học [2 TC]',
        lop='HL-1',
        lop_hp='211TKY_01001207',
        ngay_thi='07/05/2022',
        ngay='      ',
        thang='      ',
        nam='2022',
        footer='STAT1002-2021-YRD-1',
        lan_thi='2'
    )


def write_STAT1003_2021_KX_3_KX_2019_LAN1():
    response = rh.read_response(const.PATH_RESPONSE, course_id='STAT1003-2021-KX-3')
    attendee = rh.read_attendee(const.PATH_ATTENDEE_KX_2019_LAN1)
    df = mh.calc(
        attendee=attendee, response=response,
        course_id='STAT1003-2021-KX-3',
        vt_vp={
            'vt1': const.VT_KX_2019_LAN1, 'vp1': const.VP_KX_2019_LAN1,
            'vt2': const.VT_KX_2019_LAN2, 'vp2': const.VP_KX_2019_LAN2,
        })
    # df.to_excel('foo.xlsx')
    # show_cols = [0] + list(range(8,16))
    # print(df.info())
    # print(df.iloc[:, show_cols].sample(5))
    # print(df[df['STAT1001-2021-KX-2-THI1'].isna()])
    # print(df.query('user_id == "2056990004"').iloc[:, show_cols])

    wh.write_mau_import_diem_STAT1001(
        df,
        path=const.PATH_MAU_IMPORT_DIEM_KX_2019_LAN1,
        mon='Tin học nâng cao [2 TC]',
        lop='KX-2019',
        lop_hp='211THN01990101'
    )

    wh.write_bang_diem_STAT1001(
        df,
        path=const.PATH_BANG_DIEM_KX_2019_LAN1,
        mon='Tin học nâng cao [2 TC]',
        lop='KX-2019',
        lop_hp='211THN01990101',
        ngay_thi='22/03/2022',
        ngay='      ',
        thang='      ',
        nam='2022',
        footer='STAT1003-2021-KX-3'
    )

def write_STAT1001_2021_KT_2_KT_2020_LAN1():
    response = rh.read_response(const.PATH_RESPONSE, course_id='STAT1001-2021-KT-2')
    attendee = rh.read_attendee(const.PATH_ATTENDEE_KT_2020_LAN1)
    df = mh.calc(
        attendee=attendee, response=response,
        course_id='STAT1001-2021-KT-2',
        vt_vp={
            'vt1': const.VT_KT_2020_LAN1, 'vp1': const.VP_KT_2020_LAN1,
            'vt2': const.VT_KT_2020_LAN2, 'vp2': const.VP_KT_2020_LAN2,
        })
    # df.to_excel('foo.xlsx')
    # show_cols = [0] + list(range(8,16))
    # print(df.info())
    # print(df.iloc[:, show_cols].sample(5))
    # print(df[df['STAT1001-2021-KX-2-THI1'].isna()])
    # print(df.query('user_id == "2056990004"').iloc[:, show_cols])

    wh.write_mau_import_diem_STAT1001(
        df,
        path=const.PATH_MAU_IMPORT_DIEM_KT_2020_LAN1,
        mon='Xác suất - Thống kê y học [2 TC]',
        lop='KT-2020',
        lop_hp='212XST01070701',
        lan_thi='1',
    )

    wh.write_bang_diem_STAT1001(
        df,
        path=const.PATH_BANG_DIEM_KT_2020_LAN1,
        mon='Xác suất - Thống kê y học [2 TC]',
        lop='KT-2020',
        lop_hp='212XST01070701',
        ngay_thi='04/06/2022',
        ngay='      ',
        thang='      ',
        nam='2022',
        footer='STAT1001-2021-KT-2',
        lan_thi='1',
    )

def write_STAT1001_2021_YT_1_YT_2021_LAN1():
    response = rh.read_response(const.PATH_RESPONSE, course_id='STAT1001-2021-YT-1')
    attendee = rh.read_attendee(const.PATH_ATTENDEE_YT_2021_LAN1)
    df = mh.calc(
        attendee=attendee, response=response,
        course_id='STAT1001-2021-YT-1',
        vt_vp={
            'vt1': const.VT_YT_2021_LAN1, 'vp1': const.VP_YT_2021_LAN1,
            'vt2': const.VT_YT_2021_LAN2, 'vp2': const.VP_YT_2021_LAN2,
        })
    # df.to_excel('foo.xlsx')
    # show_cols = [0] + list(range(8,16))
    # print(df.info())
    # print(df.iloc[:, show_cols].sample(5))
    # print(df[df['STAT1001-2021-KX-2-THI1'].isna()])
    # print(df.query('user_id == "2056990004"').iloc[:, show_cols])

    wh.write_mau_import_diem_STAT1001(
        df,
        path=const.PATH_MAU_IMPORT_DIEM_YT_2021_LAN1,
        mon='Xác Suất - Thống Kê Y Học [2 TC]',
        lop='YT-2021',
        lop_hp='212XST01991402',
        lan_thi='1',
    )

    wh.write_bang_diem_STAT1001(
        df,
        path=const.PATH_BANG_DIEM_YT_2021_LAN1,
        mon='Xác Suất - Thống Kê Y Học [2 TC]',
        lop='YT-2021',
        lop_hp='212XST01991402',
        ngay_thi='04/06/2022',
        ngay='      ',
        thang='      ',
        nam='2022',
        footer='STAT1001-2021-YT-1',
        lan_thi='1',
    )

def write_STAT1001_2021_YT_1_YT_2019_LAN1():
    response = rh.read_response(const.PATH_RESPONSE, course_id='STAT1001-2021-YT-1')
    attendee = rh.read_attendee(const.PATH_ATTENDEE_YT_2019_LAN1)
    df = mh.calc(
        attendee=attendee, response=response,
        course_id='STAT1001-2021-YT-1',
        vt_vp={
            'vt1': const.VT_YT_2019_LAN1, 'vp1': const.VP_YT_2019_LAN1,
            'vt2': const.VT_YT_2019_LAN2, 'vp2': const.VP_YT_2019_LAN2,
        })
    # df.to_excel('foo.xlsx')
    # show_cols = [0] + list(range(8,16))
    # print(df.info())
    # print(df.iloc[:, show_cols].sample(5))
    # print(df[df['STAT1001-2021-KX-2-THI1'].isna()])
    # print(df.query('user_id == "2056990004"').iloc[:, show_cols])

    wh.write_mau_import_diem_STAT1001(
        df,
        path=const.PATH_MAU_IMPORT_DIEM_YT_2019_LAN1,
        mon='Xác Suất - Thống Kê Y Học [2 TC]',
        lop='YT-2019',
        lop_hp='212XST01991402',
        lan_thi='1',
    )

    wh.write_bang_diem_STAT1001(
        df,
        path=const.PATH_BANG_DIEM_YT_2019_LAN1,
        mon='Xác Suất - Thống Kê Y Học [2 TC]',
        lop='YT-2019',
        lop_hp='',
        ngay_thi='04/06/2022',
        ngay='      ',
        thang='      ',
        nam='2022',
        footer='STAT1001-2021-YT-1',
        lan_thi='1',
    )



def main():
    # write_STAT1001_2021_KX_2_KX_2021_LAN1()
    # write_STAT1001_2021_KX_2_DD_2018_LAN1()
    # write_STAT1001_2021_KX_2_KX_2021_LAN2()
    # write_STAT1001_2021_KX_2_DD_2018_LAN2()  # 1853010033: TB 4.7, float precision
    write_STAT1002_2021_YRD_1_Y_2021_LAN1()
    write_STAT1002_2021_YRD_1_RHM_2021_LAN1()
    write_STAT1002_2021_YRD_1_DUOC_2021_LAN1()
    write_STAT1002_2021_YRD_1_HL_1_LAN1()
    write_STAT1002_2021_YRD_1_Y_2021_LAN2()
    write_STAT1002_2021_YRD_1_RHM_2021_LAN2()
    write_STAT1002_2021_YRD_1_HL_1_LAN2()
    # write_STAT1003_2021_KX_3_KX_2019_LAN1()
    write_STAT1001_2021_KT_2_KT_2020_LAN1()
    write_STAT1001_2021_YT_1_YT_2021_LAN1()
    write_STAT1001_2021_YT_1_YT_2019_LAN1()
    pass

if __name__ == '__main__':
    main()