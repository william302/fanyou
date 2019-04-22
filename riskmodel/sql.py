from riskmodel.models import UserBase, RiskItem, RiskDetail, GreyListDetail, PlatformDetail, FrequencyDetail


def insert_frequency_detail(rdid, fd, r_type):
    for item in fd:
        print("start insert_frequency_detail")
        detail = item['detail']
        freq_d = FrequencyDetail(risk_detail_id=rdid, detail=detail, type=r_type)
        freq_d.save()


def insert_greylistdetail(rdid, grey_list, r_type):
    '''
    :param rdid: Risk_detail table's id
    :param grey_list: List of grey_list
    :param r_type: Type of riskdetail
    :return: Insert info into grey_list_detail table
    '''
    for item in grey_list:
        print("start insert_greylistdetail")
        evt = item['evidence_time']
        ril = item['risk_level']
        ft = item['fraud_type']
        ftdn = item['fraud_type_display_name']
        gld = GreyListDetail(risk_detail_id=rdid, evidence_time=evt, risk_level=ril, fraud_type=ft,
                             fraud_type_display_name=ftdn, type=r_type)
        gld.save()


def insert_platform_detail(rdid, pdl, r_type):
    '''
    :param rdid: Risk_detail table's id
    :param pd: List of platform_detail
    :param r_type: Type of riskdetail
    :return: Insert info into platform_detail table
    '''
    for item in pdl:
        print("start insert_platform_detail")
        count = item['count']
        idn = item['industry_display_name']
        pd = PlatformDetail(risk_detail_id=rdid, industry_display_name=idn, count=count, type=r_type)
        pd.save()


def insert_riskdetail(riid, risk_detail):
    '''
    :param ri_id:  RiskItem table's id
    :param risk_details: List of risk_details
    :return: insert info into risk_detail table,then denpend on type of risk_detail call insert_greylistdetail or
    insert_platform_detail function
    '''
    risk_detail = risk_detail[0]
    r_type = risk_detail['type']
    if risk_detail['type'] == 'grey_list':
        print("start insert_riskdetail___grey")
        desc = risk_detail['description']
        htdn = risk_detail['hit_type_display_name']
        frdn = risk_detail['fraud_type_display_name']
        rd = RiskDetail(risk_item_id=riid, hit_type_display_name=htdn, fraud_type_display_name=frdn, description=desc,
                        type=r_type)
        rd.save()
        grey_list_details = risk_detail['grey_list_details']
        insert_greylistdetail(rd, grey_list_details, r_type)
    elif risk_detail['type'] == 'platform_detail':
        print("start insert_riskdetail____platform")
        desc = risk_detail['description']
        count = risk_detail['platform_count']
        rd = RiskDetail(risk_item_id=riid, description=desc, type=r_type, platform_count=count)
        rd.save()
        platform_detail = risk_detail['platform_detail']
        insert_platform_detail(rd, platform_detail, r_type)
    elif risk_detail['type'] == 'frequency_detail':
        print("start insert_riskdetail___frequency_detail")
        rd = RiskDetail(risk_item_id=riid, type=r_type)
        rd.save()
        frequency_detail = risk_detail['frequency_detail_list']
        insert_frequency_detail(rd, frequency_detail, r_type)

    else:
        print("there is more type of risk_detail")


def insert_riskitem(user, risk_items):
    '''
    :param user_id: UserBase table's id
    :param risk_items: List of risk_items
    :return: insert info into risk_item table
    '''
    for item in risk_items:
        print("start insert_riskitem")
        score = item['score']
        risk_name = item['risk_name']
        decision = item['decision']
        risk_item = RiskItem(user_id=user, score=score, risk_name=risk_name, decision=decision)
        risk_item.save()
        if 'risk_detail' in item:
            risk_detail = item['risk_detail']
            insert_riskdetail(risk_item, risk_detail)


def insert_userbase(name, phone, id_num, result):
    '''
    :param name: user's name
    :param phone: user's mobile phone
    :param id_num: user's ID number
    :param result: a dictionary
    :return: insert info into userbase table
    '''

    print("start insert_userbase")
    credit_score = result['result_desc']['DEFAULT_MODEL']['b1a14f3fe5013fe3']['credit_score']
    final_score = result['result_desc']['RENT']['final_score']
    final_decision = result['result_desc']['RENT']['final_decision']
    guard_id = result['id']
    user = UserBase(name=name, phone=phone, id_number=id_num, credit_score=credit_score, final_score=final_score,
                    final_decision=final_decision, guard_id=guard_id)
    user.save()
    risk_items = result['result_desc']['RENT']['risk_items']
    insert_riskitem(user, risk_items)