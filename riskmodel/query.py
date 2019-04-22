from django.db import connection


def final_decision_chart():
    pre_stat = '''SELECT final_decision, COUNT(final_decision) from riskmodel_userbase group by final_decision'''
    with connection.cursor() as cursor:
        cursor.execute(pre_stat)
        row = cursor.fetchall()
    return row


def risk_item_chart():
    pre_stat = '''select risk_name, count(risk_name) from riskmodel_riskitem group by risk_name'''
    with connection.cursor() as cursor:
        cursor.execute(pre_stat)
        row = cursor.fetchall()
    return row