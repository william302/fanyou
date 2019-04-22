import requests
import json
from riskmodel.sql import insert_userbase


def get_tongdun_res(l):
    '''
    :param name:
    :param phone:
    :param id_num:
    :return:
    '''
    send_url = '''
                https://api.tongdun.cn/bodyguard/apply/v4.5?partner_code=s%&partner_key=%s&app_name=s%
                '''
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    r = requests.post(send_url, data={'account_name': l[0],
                                      'account_mobile': l[1],
                                      'id_number': l[2]}, headers=headers)

    result = json.loads(r.text)
    print(result)
    return result