import read_helper as rh
import mark_helper as mh
import write_helper as wh
import const

def write_INFO1001_2021_KX_1_KX_2021_LAN_1():
    response = rh.read_response(const.PATH_RESPONSE, course_id='INFO1001-2021-KX-1')
    attendee = rh.read_attendee(const.PATH_ATTENDEE_KX_2021_LAN1)
    df = mh.calc(
        attendee=attendee, response=response,
        course_id='INFO1001-2021-KX-1',
        vt_vp = {
            'vtlt1': const.VTLT_KX_2021_LAN1, 'vplt1': const.VPLT_KX_2021_LAN1, 
            'vtth1': const.VTTH_KX_2021_LAN1, 'vpth1': const.VPTH_KX_2021_LAN1,
            'vtlt2': const.VTLT_KX_2021_LAN2, 'vplt2': const.VPLT_KX_2021_LAN2, 
            'vtth2': const.VTTH_KX_2021_LAN2, 'vpth2': const.VPTH_KX_2021_LAN2,
        })
    # df.to_excel('foo.xlsx')

    wh.write_mau_import_diem_INFO1001(
        df,
        path=const.PATH_MAU_IMPORT_DIEM_KX_2021_LAN1,
        mon='Tin học [2TC]',
        lop='KX-2021',
        lop_hp='211THC_01080701',
        lan_thi='1'
    )

    wh.write_bang_diem_INFO1001(
        df,
        path=const.PATH_BANG_DIEM_KX_2021_LAN1,
        mon='Tin học [2TC]',
        lop='KX-2021',
        lop_hp='211THC_01080701',
        ngay_thi='19/02/2022',
        ngay='      ',
        thang='03',
        nam='2022',
        lan_thi='1',
        footer='INFO1001-2021-KX-1',
    )

def write_INFO1001_2021_KX_1_KX_2021_LAN_2():
    response = rh.read_response(const.PATH_RESPONSE, course_id='INFO1001-2021-KX-1')
    attendee = rh.read_attendee(const.PATH_ATTENDEE_KX_2021_LAN2)
    df = mh.calc(
        attendee=attendee, response=response,
        course_id='INFO1001-2021-KX-1',
        vt_vp = {
            'vtlt1': const.VTLT_KX_2021_LAN1, 'vplt1': const.VPLT_KX_2021_LAN1, 
            'vtth1': const.VTTH_KX_2021_LAN1, 'vpth1': const.VPTH_KX_2021_LAN1,
            'vtlt2': const.VTLT_KX_2021_LAN2, 'vplt2': const.VPLT_KX_2021_LAN2, 
            'vtth2': const.VTTH_KX_2021_LAN2, 'vpth2': const.VPTH_KX_2021_LAN2,
        })
    # df.to_excel('foo.xlsx')
    wh.write_mau_import_diem_INFO1001(
        df,
        path=const.PATH_MAU_IMPORT_DIEM_KX_2021_LAN2,
        mon='Tin học [2TC]',
        lop='KX-2021',
        lop_hp='211THC_01080701',
        lan_thi='2'
    )

    wh.write_bang_diem_INFO1001(
        df,
        path=const.PATH_BANG_DIEM_KX_2021_LAN2,
        mon='Tin học [2TC]',
        lop='KX-2021',
        lop_hp='211THC_01080701',
        ngay_thi='10/03/2022',
        ngay='      ',
        thang='03',
        nam='2022',
        lan_thi='2',
        footer='INFO1001-2021-KX-1',
    )

def write_INFO1001_2021_DD_1_DD_2021_LAN_1():
    response = rh.read_response(const.PATH_RESPONSE, course_id='INFO1001-2021-DD-1')
    attendee = rh.read_attendee(const.PATH_ATTENDEE_DD_2021_LAN1)
    df = mh.calc(
        attendee=attendee, response=response,
        course_id='INFO1001-2021-DD-1',
        vt_vp = {
            'vtlt1': const.VTLT_DD_2021_LAN1, 'vplt1': const.VPLT_DD_2021_LAN1, 
            'vtth1': const.VTTH_DD_2021_LAN1, 'vpth1': const.VPTH_DD_2021_LAN1,
            'vtlt2': const.VTLT_DD_2021_LAN2, 'vplt2': const.VPLT_DD_2021_LAN2, 
            'vtth2': const.VTTH_DD_2021_LAN2, 'vpth2': const.VPTH_DD_2021_LAN2,
        })
    # df.to_excel('foo.xlsx')
    wh.write_mau_import_diem_INFO1001(
        df,
        path=const.PATH_MAU_IMPORT_DIEM_DD_2021_LAN1,
        mon='Tin học [2TC]',
        lop='DD-2021',
        lop_hp='211THA01990701',
        lan_thi='1'
    )

    wh.write_bang_diem_INFO1001(
        df,
        path=const.PATH_BANG_DIEM_DD_2021_LAN1,
        mon='Tin học [2TC]',
        lop='DD-2021',
        lop_hp='211THA01990701',
        ngay_thi='19/02/2022',
        ngay='      ',
        thang='03',
        nam='2022',
        lan_thi='1',
        footer='INFO1001-2021-DD-1',
    )

def write_INFO1001_2021_DD_1_DD_2021_LAN_2():
    response = rh.read_response(const.PATH_RESPONSE, course_id='INFO1001-2021-DD-1')
    attendee = rh.read_attendee(const.PATH_ATTENDEE_DD_2021_LAN2)
    df = mh.calc(
        attendee=attendee, response=response,
        course_id='INFO1001-2021-DD-1',
        vt_vp = {
            'vtlt1': const.VTLT_DD_2021_LAN1, 'vplt1': const.VPLT_DD_2021_LAN1, 
            'vtth1': const.VTTH_DD_2021_LAN1, 'vpth1': const.VPTH_DD_2021_LAN1,
            'vtlt2': const.VTLT_DD_2021_LAN2, 'vplt2': const.VPLT_DD_2021_LAN2, 
            'vtth2': const.VTTH_DD_2021_LAN2, 'vpth2': const.VPTH_DD_2021_LAN2,
        })
    # print(df.query('user_id == "2053010005"'))
    df.to_excel('foo.xlsx')
    wh.write_mau_import_diem_INFO1001(
        df,
        path=const.PATH_MAU_IMPORT_DIEM_DD_2021_LAN2,
        mon='Tin học [2TC]',
        lop='DD-2021',
        lop_hp='211THA01990701',
        lan_thi='2'
    )

    wh.write_bang_diem_INFO1001(
        df,
        path=const.PATH_BANG_DIEM_DD_2021_LAN2,
        mon='Tin học [2TC]',
        lop='DD-2021',
        lop_hp='211THA01990701',
        ngay_thi='10/03/2022',
        ngay='      ',
        thang='03',
        nam='2022',
        lan_thi='2',
        footer='INFO1001-2021-DD-1',
    )

def write_INFO1001_2021_DD_1_DD_2018_LAN_1():
    response = rh.read_response(const.PATH_RESPONSE, course_id='INFO1001-2021-DD-1')
    attendee = rh.read_attendee(const.PATH_ATTENDEE_DD_2018_LAN1)
    df = mh.calc(
        attendee=attendee, response=response,
        course_id='INFO1001-2021-DD-1',
        vt_vp = {
            'vtlt1': const.VTLT_DD_2018_LAN1, 'vplt1': const.VPLT_DD_2018_LAN1, 
            'vtth1': const.VTTH_DD_2018_LAN1, 'vpth1': const.VPTH_DD_2018_LAN1,
            'vtlt2': const.VTLT_DD_2018_LAN2, 'vplt2': const.VPLT_DD_2018_LAN2, 
            'vtth2': const.VTTH_DD_2018_LAN2, 'vpth2': const.VPTH_DD_2018_LAN2,
        })
    # df.to_excel('foo.xlsx')
    wh.write_mau_import_diem_INFO1001(
        df,
        path=const.PATH_MAU_IMPORT_DIEM_DD_2018_LAN1,
        mon='Tin học [2TC]',
        lop='DD-2018',
        lop_hp='',
        lan_thi='1'
    )

    wh.write_bang_diem_INFO1001(
        df,
        path=const.PATH_BANG_DIEM_DD_2018_LAN1,
        mon='Tin học [2TC]',
        lop='DD-2018',
        lop_hp='',
        ngay_thi='19/02/2022',
        ngay='      ',
        thang='03',
        nam='2022',
        lan_thi='1',
        footer='INFO1001-2021-DD-1',
    )

def write_INFO1001_2021_DD_1_DD_2018_LAN_2():
    response = rh.read_response(const.PATH_RESPONSE, course_id='INFO1001-2021-DD-1')
    attendee = rh.read_attendee(const.PATH_ATTENDEE_DD_2018_LAN2)
    df = mh.calc(
        attendee=attendee, response=response,
        course_id='INFO1001-2021-DD-1',
        vt_vp = {
            'vtlt1': const.VTLT_DD_2018_LAN1, 'vplt1': const.VPLT_DD_2018_LAN1, 
            'vtth1': const.VTTH_DD_2018_LAN1, 'vpth1': const.VPTH_DD_2018_LAN1,
            'vtlt2': const.VTLT_DD_2018_LAN2, 'vplt2': const.VPLT_DD_2018_LAN2, 
            'vtth2': const.VTTH_DD_2018_LAN2, 'vpth2': const.VPTH_DD_2018_LAN2,
        })
    # print(df.query('user_id == "2053010005"'))
    df.to_excel('foo.xlsx')
    wh.write_mau_import_diem_INFO1001(
        df,
        path=const.PATH_MAU_IMPORT_DIEM_DD_2018_LAN2,
        mon='Tin học [2TC]',
        lop='DD-2018',
        lop_hp='',
        lan_thi='2'
    )

    wh.write_bang_diem_INFO1001(
        df,
        path=const.PATH_BANG_DIEM_DD_2018_LAN2,
        mon='Tin học [2TC]',
        lop='DD-2018',
        lop_hp='',
        ngay_thi='10/03/2022',
        ngay='      ',
        thang='03',
        nam='2022',
        lan_thi='2',
        footer='INFO1001-2021-KX-1',
    )

def write_INFO1001_2021_DHD_1_DHD_2021_LAN_1():
    response = rh.read_response(const.PATH_RESPONSE, course_id='INFO1001-2021-DHD-1')
    attendee = rh.read_attendee(const.PATH_ATTENDEE_DHD_2021_LAN1)
    df = mh.calc(
        attendee=attendee, response=response,
        course_id='INFO1001-2021-DHD-1',
        vt_vp = {
            'vtlt1': const.VTLT_DHD_2021_LAN1, 'vplt1': const.VPLT_DHD_2021_LAN1, 
            'vtth1': const.VTTH_DHD_2021_LAN1, 'vpth1': const.VPTH_DHD_2021_LAN1,
            'vtlt2': const.VTLT_DHD_2021_LAN2, 'vplt2': const.VPLT_DHD_2021_LAN2, 
            'vtth2': const.VTTH_DHD_2021_LAN2, 'vpth2': const.VPTH_DHD_2021_LAN2,
        })
    # df.to_excel('foo.xlsx')
    wh.write_mau_import_diem_INFO1001(
        df,
        path=const.PATH_MAU_IMPORT_DIEM_DHD_2021_LAN1,
        mon='Tin học đại cương [2 TC]',
        lop='DHD-2021',
        lop_hp='211TDC01991002',
        lan_thi='1',
    )

    wh.write_bang_diem_INFO1001(
        df,
        path=const.PATH_BANG_DIEM_DHD_2021_LAN1,
        mon='Tin học đại cương [2 TC]',
        lop='DHD-2021',
        lop_hp='211TDC01991002',
        lan_thi='1',
        ngay_thi='19/02/2022',
        ngay='      ',
        thang='03',
        nam='2022',
        footer='INFO1001-2021-DHD-1',
    )

def write_INFO1001_2021_DHD_1_DHD_2021_LAN_2():
    response = rh.read_response(const.PATH_RESPONSE, course_id='INFO1001-2021-DHD-1')
    attendee = rh.read_attendee(const.PATH_ATTENDEE_DHD_2021_LAN2)
    df = mh.calc(
        attendee=attendee, response=response,
        course_id='INFO1001-2021-DHD-1',
        vt_vp = {
            'vtlt1': const.VTLT_DHD_2021_LAN1, 'vplt1': const.VPLT_DHD_2021_LAN1, 
            'vtth1': const.VTTH_DHD_2021_LAN1, 'vpth1': const.VPTH_DHD_2021_LAN1,
            'vtlt2': const.VTLT_DHD_2021_LAN2, 'vplt2': const.VPLT_DHD_2021_LAN2, 
            'vtth2': const.VTTH_DHD_2021_LAN2, 'vpth2': const.VPTH_DHD_2021_LAN2,
        })
    # print(df.query('user_id == "2053010005"'))
    df.to_excel('foo.xlsx')
    wh.write_mau_import_diem_INFO1001(
        df,
        path=const.PATH_MAU_IMPORT_DIEM_DHD_2021_LAN2,
        mon='Tin học đại cương [2 TC]',
        lop='DHD-2021',
        lop_hp='211TDC01991002',
        lan_thi='2',
    )

    wh.write_bang_diem_INFO1001(
        df,
        path=const.PATH_BANG_DIEM_DHD_2021_LAN2,
        mon='Tin học đại cương [2 TC]',
        lop='DHD-2021',
        lop_hp='211TDC01991002',
        lan_thi='2',
        ngay_thi='10/03/2022',
        ngay='      ',
        thang='03',
        nam='2022',
        footer='INFO1001-2021-DHD-1',
    )

def write_INFO1001_2021_KT_1_KT_2021_LAN_1():
    response = rh.read_response(const.PATH_RESPONSE, course_id='INFO1001-2021-KT-1')
    attendee = rh.read_attendee(const.PATH_ATTENDEE_KT_2021_LAN1)
    df = mh.calc(
        attendee=attendee, response=response,
        course_id='INFO1001-2021-KT-1',
        vt_vp = {
            'vtlt1': const.VTLT_KT_2021_LAN1, 'vplt1': const.VPLT_KT_2021_LAN1, 
            'vtth1': const.VTTH_KT_2021_LAN1, 'vpth1': const.VPTH_KT_2021_LAN1,
            'vtlt2': const.VTLT_KT_2021_LAN2, 'vplt2': const.VPLT_KT_2021_LAN2, 
            'vtth2': const.VTTH_KT_2021_LAN2, 'vpth2': const.VPTH_KT_2021_LAN2,
        })
    # df.to_excel('foo.xlsx')

    wh.write_mau_import_diem_INFO1001(
        df,
        path=const.PATH_MAU_IMPORT_DIEM_KT_2021_LAN1,
        mon='Tin học [2TC]',
        lop='KT-2021',
        lop_hp='211TIN01070301',
        lan_thi='1'
    )

    wh.write_bang_diem_INFO1001(
        df,
        path=const.PATH_BANG_DIEM_KT_2021_LAN1,
        mon='Tin học [2TC]',
        lop='KT-2021',
        lop_hp='211TIN01070301',
        ngay_thi='19/02/2022',
        ngay='      ',
        thang='03',
        nam='2022',
        lan_thi='1',
        footer='INFO1001-2021-KT-1',
    )

def write_INFO1001_2021_KT_1_KT_2021_LAN_2():
    response = rh.read_response(const.PATH_RESPONSE, course_id='INFO1001-2021-KT-1')
    attendee = rh.read_attendee(const.PATH_ATTENDEE_KT_2021_LAN2)
    df = mh.calc(
        attendee=attendee, response=response,
        course_id='INFO1001-2021-KT-1',
        vt_vp = {
            'vtlt1': const.VTLT_KT_2021_LAN1, 'vplt1': const.VPLT_KT_2021_LAN1, 
            'vtth1': const.VTTH_KT_2021_LAN1, 'vpth1': const.VPTH_KT_2021_LAN1,
            'vtlt2': const.VTLT_KT_2021_LAN2, 'vplt2': const.VPLT_KT_2021_LAN2, 
            'vtth2': const.VTTH_KT_2021_LAN2, 'vpth2': const.VPTH_KT_2021_LAN2,
        })
    # df.to_excel('foo.xlsx')
    wh.write_mau_import_diem_INFO1001(
        df,
        path=const.PATH_MAU_IMPORT_DIEM_KT_2021_LAN2,
        mon='Tin học [2TC]',
        lop='KT-2021',
        lop_hp='211TIN01070301',
        lan_thi='2'
    )

    wh.write_bang_diem_INFO1001(
        df,
        path=const.PATH_BANG_DIEM_KT_2021_LAN2,
        mon='Tin học [2TC]',
        lop='KT-2021',
        lop_hp='211TIN01070301',
        ngay_thi='10/03/2022',
        ngay='      ',
        thang='03',
        nam='2022',
        lan_thi='2',
        footer='INFO1001-2021-KT-1',
    )

def write_INFO1001_2021_XN_1_XN_2021_LAN_1():
    response = rh.read_response(const.PATH_RESPONSE, course_id='INFO1001-2021-XN-1')
    attendee = rh.read_attendee(const.PATH_ATTENDEE_XN_2021_LAN1)
    df = mh.calc(
        attendee=attendee, response=response,
        course_id='INFO1001-2021-XN-1',
        vt_vp = {
            'vtlt1': const.VTLT_XN_2021_LAN1, 'vplt1': const.VPLT_XN_2021_LAN1, 
            'vtth1': const.VTTH_XN_2021_LAN1, 'vpth1': const.VPTH_XN_2021_LAN1,
            'vtlt2': const.VTLT_XN_2021_LAN2, 'vplt2': const.VPLT_XN_2021_LAN2, 
            'vtth2': const.VTTH_XN_2021_LAN2, 'vpth2': const.VPTH_XN_2021_LAN2,
        })
    # df.to_excel('foo.xlsx')

    wh.write_mau_import_diem_INFO1001(
        df,
        path=const.PATH_MAU_IMPORT_DIEM_XN_2021_LAN1,
        mon='Tin học [2TC]',
        lop='XN-2021',
        lop_hp='211THA01990703',
        lan_thi='1'
    )

    wh.write_bang_diem_INFO1001(
        df,
        path=const.PATH_BANG_DIEM_XN_2021_LAN1,
        mon='Tin học [2TC]',
        lop='XN-2021',
        lop_hp='211THA01990703',
        ngay_thi='19/02/2022',
        ngay='      ',
        thang='03',
        nam='2022',
        lan_thi='1',
        footer='INFO1001-2021-XN-1',
    )

def write_INFO1001_2021_XN_1_XN_2021_LAN_2():
    response = rh.read_response(const.PATH_RESPONSE, course_id='INFO1001-2021-XN-1')
    attendee = rh.read_attendee(const.PATH_ATTENDEE_XN_2021_LAN2)
    df = mh.calc(
        attendee=attendee, response=response,
        course_id='INFO1001-2021-XN-1',
        vt_vp = {
            'vtlt1': const.VTLT_XN_2021_LAN1, 'vplt1': const.VPLT_XN_2021_LAN1, 
            'vtth1': const.VTTH_XN_2021_LAN1, 'vpth1': const.VPTH_XN_2021_LAN1,
            'vtlt2': const.VTLT_XN_2021_LAN2, 'vplt2': const.VPLT_XN_2021_LAN2, 
            'vtth2': const.VTTH_XN_2021_LAN2, 'vpth2': const.VPTH_XN_2021_LAN2,
        })
    # df.to_excel('foo.xlsx')
    wh.write_mau_import_diem_INFO1001(
        df,
        path=const.PATH_MAU_IMPORT_DIEM_XN_2021_LAN2,
        mon='Tin học [2TC]',
        lop='XN-2021',
        lop_hp='211THA01990703',
        lan_thi='2'
    )

    wh.write_bang_diem_INFO1001(
        df,
        path=const.PATH_BANG_DIEM_XN_2021_LAN2,
        mon='Tin học [2TC]',
        lop='XN-2021',
        lop_hp='211THA01990703',
        ngay_thi='10/03/2022',
        ngay='      ',
        thang='03',
        nam='2022',
        lan_thi='2',
        footer='INFO1001-2021-XN-1',
    )

def write_INFO1001_2021_YT_1_YT_2021_LAN_1():
    response = rh.read_response(const.PATH_RESPONSE, course_id='INFO1001-2021-YT-1')
    attendee = rh.read_attendee(const.PATH_ATTENDEE_YT_2021_LAN1)
    df = mh.calc(
        attendee=attendee, response=response,
        course_id='INFO1001-2021-YT-1',
        vt_vp = {
            'vtlt1': const.VTLT_YT_2021_LAN1, 'vplt1': const.VPLT_YT_2021_LAN1, 
            'vtth1': const.VTTH_YT_2021_LAN1, 'vpth1': const.VPTH_YT_2021_LAN1,
            'vtlt2': const.VTLT_YT_2021_LAN2, 'vplt2': const.VPLT_YT_2021_LAN2, 
            'vtth2': const.VTTH_YT_2021_LAN2, 'vpth2': const.VPTH_YT_2021_LAN2,
        })
    # df.to_excel('foo.xlsx')
    wh.write_mau_import_diem_INFO1001(
        df,
        path=const.PATH_MAU_IMPORT_DIEM_YT_2021_LAN1,
        mon='Tin học đại cương [2 TC]',
        lop='YT-2021',
        lop_hp='211TDC01991001',
        lan_thi='1'
    )

    wh.write_bang_diem_INFO1001(
        df,
        path=const.PATH_BANG_DIEM_YT_2021_LAN1,
        mon='Tin học đại cương [2 TC]',
        lop='YT-2021',
        lop_hp='211TDC01991001',
        lan_thi='1',
        ngay_thi='19/02/2022',
        ngay='      ',
        thang='03',
        nam='2022',
        footer='INFO1001-2021-YT-1',
    )

def write_INFO1001_2021_YT_1_YT_2021_LAN_2():
    response = rh.read_response(const.PATH_RESPONSE, course_id='INFO1001-2021-YT-1')
    attendee = rh.read_attendee(const.PATH_ATTENDEE_YT_2021_LAN2)
    df = mh.calc(
        attendee=attendee, response=response,
        course_id='INFO1001-2021-YT-1',
        vt_vp = {
            'vtlt1': const.VTLT_YT_2021_LAN1, 'vplt1': const.VPLT_YT_2021_LAN1, 
            'vtth1': const.VTTH_YT_2021_LAN1, 'vpth1': const.VPTH_YT_2021_LAN1,
            'vtlt2': const.VTLT_YT_2021_LAN2, 'vplt2': const.VPLT_YT_2021_LAN2, 
            'vtth2': const.VTTH_YT_2021_LAN2, 'vpth2': const.VPTH_YT_2021_LAN2,
        })
    # print(df.query('user_id == "2053010005"'))
    df.to_excel('foo.xlsx')
    wh.write_mau_import_diem_INFO1001(
        df,
        path=const.PATH_MAU_IMPORT_DIEM_YT_2021_LAN2,
        mon='Tin học đại cương [2 TC]',
        lop='YT-2021',
        lop_hp='211TDC01991001',
        lan_thi='2',
    )
    wh.write_bang_diem_INFO1001(
        df,
        path=const.PATH_BANG_DIEM_YT_2021_LAN2,
        mon='Tin học đại cương [2 TC]',
        lop='YT-2021',
        lop_hp='211TDC01991001',
        lan_thi='2',
        ngay_thi='10/03/2022',
        ngay='      ',
        thang='03',
        nam='2022',
        footer='INFO1001-2021-YT-1',
    )

def write_INFO1001_2021_YRD_1_Y_2021_LAN_1():
    response = rh.read_response(const.PATH_RESPONSE, course_id='INFO1001-2021-YRD-1')
    attendee = rh.read_attendee(const.PATH_ATTENDEE_Y_2021_LAN1)
    df = mh.calc(
        attendee=attendee, response=response,
        course_id='INFO1001-2021-YRD-1',
        vt_vp = {
            'vtlt1': const.VTLT_Y_2021_LAN1, 'vplt1': const.VPLT_Y_2021_LAN1, 
            'vtth1': const.VTTH_Y_2021_LAN1, 'vpth1': const.VPTH_Y_2021_LAN1,
            'vtlt2': const.VTLT_Y_2021_LAN2, 'vplt2': const.VPLT_Y_2021_LAN2, 
            'vtth2': const.VTTH_Y_2021_LAN2, 'vpth2': const.VPTH_Y_2021_LAN2,
        })
    # df.to_excel('foo.xlsx')
    wh.write_mau_import_diem_INFO1001(
        df,
        path=const.PATH_MAU_IMPORT_DIEM_Y_2021_LAN1,
        mon='Tin học [2 TC]',
        lop='Y-2021',
        lop_hp='211TTO_01000603',
        lan_thi='1'
    )

    wh.write_bang_diem_INFO1001(
        df,
        path=const.PATH_BANG_DIEM_Y_2021_LAN1,
        mon='Tin học [2 TC]',
        lop='Y-2021',
        lop_hp='211TTO_01000603',
        lan_thi='1',
        ngay_thi='14/04/2022',
        ngay='      ',
        thang='      ',
        nam='2022',
        footer='INFO1001-2021-YRD-1',
    )

def write_INFO1001_2021_YRD_1_RHM_2021_LAN_1():
    response = rh.read_response(const.PATH_RESPONSE, course_id='INFO1001-2021-YRD-1')
    attendee = rh.read_attendee(const.PATH_ATTENDEE_RHM_2021_LAN1)
    df = mh.calc(
        attendee=attendee, response=response,
        course_id='INFO1001-2021-YRD-1',
        vt_vp = {
            'vtlt1': const.VTLT_RHM_2021_LAN1, 'vplt1': const.VPLT_RHM_2021_LAN1, 
            'vtth1': const.VTTH_RHM_2021_LAN1, 'vpth1': const.VPTH_RHM_2021_LAN1,
            'vtlt2': const.VTLT_RHM_2021_LAN2, 'vplt2': const.VPLT_RHM_2021_LAN2, 
            'vtth2': const.VTTH_RHM_2021_LAN2, 'vpth2': const.VPTH_RHM_2021_LAN2,
        })
    # df.to_excel('foo.xlsx')
    wh.write_mau_import_diem_INFO1001(
        df,
        path=const.PATH_MAU_IMPORT_DIEM_RHM_2021_LAN1,
        mon='Tin học [2 TC]',
        lop='RHM-2021',
        lop_hp='211TTO_01000605',
        lan_thi='1'
    )

    wh.write_bang_diem_INFO1001(
        df,
        path=const.PATH_BANG_DIEM_RHM_2021_LAN1,
        mon='Tin học [2 TC]',
        lop='RHM-2021',
        lop_hp='211TTO_01000605',
        lan_thi='1',
        ngay_thi='14/04/2022',
        ngay='      ',
        thang='      ',
        nam='2022',
        footer='INFO1001-2021-YRD-1',
    )

def write_INFO1001_2021_YRD_1_DUOC_2021_LAN_1():
    response = rh.read_response(const.PATH_RESPONSE, course_id='INFO1001-2021-YRD-1')
    attendee = rh.read_attendee(const.PATH_ATTENDEE_DUOC_2021_LAN1)
    df = mh.calc(
        attendee=attendee, response=response,
        course_id='INFO1001-2021-YRD-1',
        vt_vp = {
            'vtlt1': const.VTLT_DUOC_2021_LAN1, 'vplt1': const.VPLT_DUOC_2021_LAN1, 
            'vtth1': const.VTTH_DUOC_2021_LAN1, 'vpth1': const.VPTH_DUOC_2021_LAN1,
            'vtlt2': const.VTLT_DUOC_2021_LAN2, 'vplt2': const.VPLT_DUOC_2021_LAN2, 
            'vtth2': const.VTTH_DUOC_2021_LAN2, 'vpth2': const.VPTH_DUOC_2021_LAN2,
        })
    # df.to_excel('foo.xlsx')
    wh.write_mau_import_diem_INFO1001(
        df,
        path=const.PATH_MAU_IMPORT_DIEM_DUOC_2021_LAN1,
        mon='Tin học [2 TC]',
        lop='DUOC-2021',
        lop_hp='211TTO_01000601',
        lan_thi='1'
    )

    wh.write_bang_diem_INFO1001(
        df,
        path=const.PATH_BANG_DIEM_DUOC_2021_LAN1,
        mon='Tin học [2 TC]',
        lop='DUOC-2021',
        lop_hp='211TTO_01000601',
        lan_thi='1',
        ngay_thi='14/04/2022',
        ngay='      ',
        thang='      ',
        nam='2022',
        footer='INFO1001-2021-YRD-1',
    )

def write_INFO1001_2020_YRD_1_RHM_2020_LAN_2():
    response = rh.read_response(const.PATH_RESPONSE, course_id='INFO1001-2020-YRD-1')
    attendee = rh.read_attendee(const.PATH_ATTENDEE_RHM_2020_LAN2)
    df = mh.calc(
        attendee=attendee, response=response,
        course_id='INFO1001-2020-YRD-1',
        vt_vp = {
            'vtlt1': const.VTLT_RHM_2020_LAN2, 'vplt1': const.VPLT_RHM_2020_LAN2, 
            'vtth1': const.VTTH_RHM_2020_LAN2, 'vpth1': const.VPTH_RHM_2020_LAN2,
            'vtlt2': const.VTLT_RHM_2020_LAN2, 'vplt2': const.VPLT_RHM_2021_LAN2, 
            'vtth2': const.VTTH_RHM_2020_LAN2, 'vpth2': const.VPTH_RHM_2021_LAN2,
        })
    # df.to_excel('foo.xlsx')
    wh.write_mau_import_diem_INFO1001(
        df,
        path=const.PATH_MAU_IMPORT_DIEM_RHM_2020_LAN2,
        mon='Tin học [2 TC]',
        lop='RHM-2020',
        lop_hp='',
        lan_thi='2'
    )

    wh.write_bang_diem_INFO1001(
        df,
        path=const.PATH_BANG_DIEM_RHM_2020_LAN2,
        mon='Tin học [2 TC]',
        lop='RHM-2020',
        lop_hp='',
        lan_thi='2',
        ngay_thi='14/04/2022',
        ngay='      ',
        thang='      ',
        nam='2022',
        footer='INFO1001-2020-YRD-1',
    )

def write_INFO1001_2021_YRD_1_HL_1_LAN_1():
    response = rh.read_response(const.PATH_RESPONSE, course_id='INFO1001-2021-YRD-1')
    attendee = rh.read_attendee(const.PATH_ATTENDEE_HL_1_LAN1)
    df = mh.calc(
        attendee=attendee, response=response,
        course_id='INFO1001-2021-YRD-1',
        vt_vp = {
            'vtlt1': const.VTLT_HL_1_LAN1, 'vplt1': const.VPLT_HL_1_LAN1, 
            'vtth1': const.VTTH_HL_1_LAN1, 'vpth1': const.VPTH_HL_1_LAN1,
            'vtlt2': const.VTLT_HL_1_LAN2, 'vplt2': const.VPLT_HL_1_LAN2, 
            'vtth2': const.VTTH_HL_1_LAN2, 'vpth2': const.VPTH_HL_1_LAN2,
        })
    
    wh.write_mau_import_diem_INFO1001(
        df,
        path=const.PATH_MAU_IMPORT_DIEM_HL_1_LAN1,
        mon='Tin học [2 TC]',
        lop='HL-1',
        lop_hp='211TTO_01000607',
        lan_thi='1'
    )

    wh.write_bang_diem_INFO1001(
        df,
        path=const.PATH_BANG_DIEM_HL_1_LAN1,
        mon='Tin học [2 TC]',
        lop='HL-1',
        lop_hp='211TTO_01000607',
        lan_thi='1',
        ngay_thi='14/04/2022',
        ngay='      ',
        thang='      ',
        nam='2022',
        footer='INFO1001-2021-YRD-1',
    )

def write_INFO1001_2021_YRD_1_HL_1_LAN_2_1():
    response = rh.read_response(const.PATH_RESPONSE, course_id='INFO1001-2021-YRD-1')
    attendee = rh.read_attendee(const.PATH_ATTENDEE_HL_1_LAN2_1)
    df = mh.calc(
        attendee=attendee, response=response,
        course_id='INFO1001-2021-YRD-1',
        vt_vp = {
            'vtlt1': const.VTLT_HL_1_LAN1, 'vplt1': const.VPLT_HL_1_LAN1, 
            'vtth1': const.VTTH_HL_1_LAN1, 'vpth1': const.VPTH_HL_1_LAN1,
            'vtlt2': const.VTLT_HL_1_LAN2, 'vplt2': const.VPLT_HL_1_LAN2, 
            'vtth2': const.VTTH_HL_1_LAN2, 'vpth2': const.VPTH_HL_1_LAN2,
        })
    # df.to_excel('foo.xlsx')
    wh.write_mau_import_diem_INFO1001(
        df,
        path=const.PATH_MAU_IMPORT_DIEM_HL_1_LAN2_1,
        mon='Tin học [2 TC]',
        lop='HL-1',
        lop_hp='211TTO_01000607',
        lan_thi='2'
    )

    wh.write_bang_diem_INFO1001(
        df,
        path=const.PATH_BANG_DIEM_HL_1_LAN2_1,
        mon='Tin học [2 TC]',
        lop='HL-1',
        lop_hp='211TTO_01000607',
        lan_thi='2',
        ngay_thi='10/05/2022',
        ngay='      ',
        thang='      ',
        nam='2022',
        footer='INFO1001-2021-YRD-1',
    )

def write_INFO1001_2021_YVD_1_YVD_2021_LAN_1():
    response = rh.read_response(const.PATH_RESPONSE, course_id='INFO1001-2021-YVD-1')
    attendee = rh.read_attendee(const.PATH_ATTENDEE_YVD_2021_LAN1)
    df = mh.calc(
        attendee=attendee, response=response,
        course_id='INFO1001-2021-YVD-1',
        vt_vp = {
            'vtlt1': const.VTLT_YVD_2021_LAN1, 'vplt1': const.VPLT_YVD_2021_LAN1, 
            'vtth1': const.VTTH_YVD_2021_LAN1, 'vpth1': const.VPTH_YVD_2021_LAN1,
            'vtlt2': const.VTLT_YVD_2021_LAN2, 'vplt2': const.VPLT_YVD_2021_LAN2, 
            'vtth2': const.VTTH_YVD_2021_LAN2, 'vpth2': const.VPTH_YVD_2021_LAN2,
        })
    # df.to_excel('foo.xlsx')
    wh.write_mau_import_diem_INFO1001(
        df,
        path=const.PATH_MAU_IMPORT_DIEM_YVD_2021_LAN1,
        mon='Tin học [2 TC]',
        lop='YVD-2021',
        lop_hp='',
        lan_thi='1'
    )

    wh.write_bang_diem_INFO1001(
        df,
        path=const.PATH_BANG_DIEM_YVD_2021_LAN1,
        mon='Tin học [2 TC]',
        lop='YVD-2021',
        lop_hp='',
        lan_thi='1',
        ngay_thi='06/06/2022',
        ngay='      ',
        thang='      ',
        nam='2022',
        footer='INFO1001-2021-YVD-1',
    )

# def write_INFO1001_2021_YVD_1_YVD_2021_LAN_2():
#     response = rh.read_response(const.PATH_RESPONSE, course_id='INFO1001-2021-YVD-1')
#     attendee = rh.read_attendee(const.PATH_ATTENDEE_YVD_2021_LAN2)
#     df = mh.calc(
#         attendee=attendee, response=response,
#         course_id='INFO1001-2021-YVD-1',
#         vt_vp = {
#             'vtlt1': const.VTLT_YVD_2021_LAN1, 'vplt1': const.VPLT_YVD_2021_LAN1, 
#             'vtth1': const.VTTH_YVD_2021_LAN1, 'vpth1': const.VPTH_YVD_2021_LAN1,
#             'vtlt2': const.VTLT_YVD_2021_LAN2, 'vplt2': const.VPLT_YVD_2021_LAN2, 
#             'vtth2': const.VTTH_YVD_2021_LAN2, 'vpth2': const.VPTH_YVD_2021_LAN2,
#         })
#     # df.to_excel('foo.xlsx')
#     wh.write_mau_import_diem_INFO1001(
#         df,
#         path=const.PATH_MAU_IMPORT_DIEM_YVD_2021_LAN2,
#         mon='Tin học [2 TC]',
#         lop='YVD-2021',
#         lop_hp='',
#         lan_thi='1'
#     )

#     wh.write_bang_diem_INFO1001(
#         df,
#         path=const.PATH_BANG_DIEM_YVD_2021_LAN1,
#         mon='Tin học [2 TC]',
#         lop='YVD-2021',
#         lop_hp='',
#         lan_thi='1',
#         ngay_thi='14/04/2022',
#         ngay='      ',
#         thang='      ',
#         nam='2022',
#         footer='INFO1001-2021-YVD-1',
#     )


def write_INFO1001_2021_YRD_1_Y_2021_LAN_2():
    response = rh.read_response(const.PATH_RESPONSE, course_id='INFO1001-2021-YRD-1')
    attendee = rh.read_attendee(const.PATH_ATTENDEE_Y_2021_LAN2)
    df = mh.calc(
        attendee=attendee, response=response,
        course_id='INFO1001-2021-YRD-1',
        vt_vp = {
            'vtlt1': const.VTLT_Y_2021_LAN1, 'vplt1': const.VPLT_Y_2021_LAN1, 
            'vtth1': const.VTTH_Y_2021_LAN1, 'vpth1': const.VPTH_Y_2021_LAN1,
            'vtlt2': const.VTLT_Y_2021_LAN2, 'vplt2': const.VPLT_Y_2021_LAN2, 
            'vtth2': const.VTTH_Y_2021_LAN2, 'vpth2': const.VPTH_Y_2021_LAN2,
        })
    # df.to_excel('foo.xlsx')
    wh.write_mau_import_diem_INFO1001(
        df,
        path=const.PATH_MAU_IMPORT_DIEM_Y_2021_LAN2,
        mon='Tin học [2 TC]',
        lop='Y-2021',
        lop_hp='211TTO_01000603',
        lan_thi='2'
    )

    wh.write_bang_diem_INFO1001(
        df,
        path=const.PATH_BANG_DIEM_Y_2021_LAN2,
        mon='Tin học [2 TC]',
        lop='Y-2021',
        lop_hp='211TTO_01000603',
        lan_thi='2',
        ngay_thi='26/05/2022',
        ngay='      ',
        thang='      ',
        nam='2022',
        footer='INFO1001-2021-YRD-1',
    )
    
def write_INFO1001_2021_YRD_1_RHM_2021_LAN_2():
    response = rh.read_response(const.PATH_RESPONSE, course_id='INFO1001-2021-YRD-1')
    attendee = rh.read_attendee(const.PATH_ATTENDEE_RHM_2021_LAN2)
    df = mh.calc(
        attendee=attendee, response=response,
        course_id='INFO1001-2021-YRD-1',
        vt_vp = {
            'vtlt1': const.VTLT_RHM_2021_LAN1, 'vplt1': const.VPLT_RHM_2021_LAN1, 
            'vtth1': const.VTTH_RHM_2021_LAN1, 'vpth1': const.VPTH_RHM_2021_LAN1,
            'vtlt2': const.VTLT_RHM_2021_LAN2, 'vplt2': const.VPLT_RHM_2021_LAN2, 
            'vtth2': const.VTTH_RHM_2021_LAN2, 'vpth2': const.VPTH_RHM_2021_LAN2,
        })
    # df.to_excel('foo.xlsx')
    wh.write_mau_import_diem_INFO1001(
        df,
        path=const.PATH_MAU_IMPORT_DIEM_RHM_2021_LAN2,
        mon='Tin học [2 TC]',
        lop='RHM-2021',
        lop_hp='211TTO_01000605',
        lan_thi='2'
    )

    wh.write_bang_diem_INFO1001(
        df,
        path=const.PATH_BANG_DIEM_RHM_2021_LAN2,
        mon='Tin học [2 TC]',
        lop='RHM-2021',
        lop_hp='211TTO_01000605',
        lan_thi='2',
        ngay_thi='26/05/2022',
        ngay='      ',
        thang='      ',
        nam='2022',
        footer='INFO1001-2021-YRD-1',
    )

def write_INFO1001_2021_YRD_1_DUOC_2021_LAN_2():
    response = rh.read_response(const.PATH_RESPONSE, course_id='INFO1001-2021-YRD-1')
    attendee = rh.read_attendee(const.PATH_ATTENDEE_DUOC_2021_LAN2)
    df = mh.calc(
        attendee=attendee, response=response,
        course_id='INFO1001-2021-YRD-1',
        vt_vp = {
            'vtlt1': const.VTLT_DUOC_2021_LAN1, 'vplt1': const.VPLT_DUOC_2021_LAN1, 
            'vtth1': const.VTTH_DUOC_2021_LAN1, 'vpth1': const.VPTH_DUOC_2021_LAN1,
            'vtlt2': const.VTLT_DUOC_2021_LAN2, 'vplt2': const.VPLT_DUOC_2021_LAN2, 
            'vtth2': const.VTTH_DUOC_2021_LAN2, 'vpth2': const.VPTH_DUOC_2021_LAN2,
        })
    # df.to_excel('foo.xlsx')
    wh.write_mau_import_diem_INFO1001(
        df,
        path=const.PATH_MAU_IMPORT_DIEM_DUOC_2021_LAN2,
        mon='Tin học [2 TC]',
        lop='DUOC-2021',
        lop_hp='211TTO_01000601',
        lan_thi='2'
    )

    wh.write_bang_diem_INFO1001(
        df,
        path=const.PATH_BANG_DIEM_DUOC_2021_LAN2,
        mon='Tin học [2 TC]',
        lop='DUOC-2021',
        lop_hp='211TTO_01000601',
        lan_thi='2',
        ngay_thi='26/05/2022',
        ngay='      ',
        thang='      ',
        nam='2022',
        footer='INFO1001-2021-YRD-1',
    )

def write_INFO1001_2021_YRD_1_HL_1_LAN_2():
    response = rh.read_response(const.PATH_RESPONSE, course_id='INFO1001-2021-YRD-1')
    attendee = rh.read_attendee(const.PATH_ATTENDEE_HL_1_LAN2)
    df = mh.calc(
        attendee=attendee, response=response,
        course_id='INFO1001-2021-YRD-1',
        vt_vp = {
            'vtlt1': const.VTLT_HL_1_LAN1, 'vplt1': const.VPLT_HL_1_LAN1, 
            'vtth1': const.VTTH_HL_1_LAN1, 'vpth1': const.VPTH_HL_1_LAN1,
            'vtlt2': const.VTLT_HL_1_LAN2, 'vplt2': const.VPLT_HL_1_LAN2, 
            'vtth2': const.VTTH_HL_1_LAN2, 'vpth2': const.VPTH_HL_1_LAN2,
        })
    
    wh.write_mau_import_diem_INFO1001(
        df,
        path=const.PATH_MAU_IMPORT_DIEM_HL_1_LAN2,
        mon='Tin học [2 TC]',
        lop='HL-1',
        lop_hp='211TTO_01000607',
        lan_thi='2'
    )

    wh.write_bang_diem_INFO1001(
        df,
        path=const.PATH_BANG_DIEM_HL_1_LAN2,
        mon='Tin học [2 TC]',
        lop='HL-1',
        lop_hp='211TTO_01000607',
        lan_thi='2',
        ngay_thi='26/05/2022',
        ngay='      ',
        thang='      ',
        nam='2022',
        footer='INFO1001-2021-YRD-1',
    )
    




def main():
    # write_INFO1001_2021_KX_1_KX_2021_LAN_1()
    # write_INFO1001_2021_KX_1_KX_2021_LAN_2()
    # write_INFO1001_2021_DD_1_DD_2021_LAN_1()
    # write_INFO1001_2021_DD_1_DD_2021_LAN_2()
    # write_INFO1001_2021_DD_1_DD_2018_LAN_1()  # Khong co diem qua trinh
    # write_INFO1001_2021_DD_1_DD_2018_LAN_2()  # Khong co diem qua trinh
    # write_INFO1001_2021_DHD_1_DHD_2021_LAN_1()
    # write_INFO1001_2021_DHD_1_DHD_2021_LAN_2()
    # write_INFO1001_2021_KT_1_KT_2021_LAN_1()
    # write_INFO1001_2021_KT_1_KT_2021_LAN_2()
    # write_INFO1001_2021_XN_1_XN_2021_LAN_1()
    # write_INFO1001_2021_XN_1_XN_2021_LAN_2()
    # write_INFO1001_2021_YT_1_YT_2021_LAN_1()
    # write_INFO1001_2021_YT_1_YT_2021_LAN_2()
    write_INFO1001_2021_YRD_1_Y_2021_LAN_1()
    write_INFO1001_2021_YRD_1_RHM_2021_LAN_1()
    write_INFO1001_2021_YRD_1_DUOC_2021_LAN_1()
    # write_INFO1001_2020_YRD_1_RHM_2020_LAN_2()
    write_INFO1001_2021_YRD_1_HL_1_LAN_1()
    # write_INFO1001_2021_YRD_1_HL_1_LAN_2_1()
    write_INFO1001_2021_YVD_1_YVD_2021_LAN_1()
    write_INFO1001_2021_YRD_1_Y_2021_LAN_2()
    write_INFO1001_2021_YRD_1_RHM_2021_LAN_2()
    write_INFO1001_2021_YRD_1_DUOC_2021_LAN_2()
    write_INFO1001_2021_YRD_1_HL_1_LAN_2()
    pass

if __name__ == '__main__':
    main()