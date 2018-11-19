import datetime
from django.db import connection


def find_user(phone):
    sql = "SELECT merchant_id FROM t_user_base WHERE mobile = %s"
    args = (phone,)
    with connection.cursor() as cursor:
        cursor.execute(sql, args)
        row = cursor.fetchone()
    return row


def insert_user(phone, dealer_id):
    current_time = datetime.datetime.now()
    sql = '''INSERT INTO t_user_base(mobile, merchant_id,last_login_time, add_time) VALUES(%s, %s, %s, %s)'''
    args = [phone, dealer_id, current_time, current_time]
    with connection.cursor() as cursor:
        cursor.execute(sql, args)
        connection.commit()
    return


def update_user(phone, dealer_id):
    sql = "UPDATE t_user_base SET merchant_id = %s WHERE mobile = %s"
    args = [dealer_id, phone]
    with connection.cursor() as cursor:
        cursor.execute(sql, args)
        connection.commit()
    return


def find_merchant_user(dealer_id):
    sql = "SELECT u.card_name, u.mobile FROM blog_merchant AS m INNER JOIN t_user_base AS u ON u.merchant_id = m.id WHERE m.id = %s"
    args = (dealer_id,)
    with connection.cursor() as cursor:
        cursor.execute(sql, args)
        rows = cursor.fetchall()
    return rows


def find_user_voted_time(phone):
    sql = "SELECT voted_time FROM t_user_base WHERE mobile = %s"
    args = (phone,)
    with connection.cursor() as cursor:
        cursor.execute(sql, args)
        row = cursor.fetchone()
    return row[0]


def update_user_voted_time(phone):
    sql = "UPDATE t_user_base SET voted_time = %s, is_voted=1 WHERE mobile = %s"
    current_time = datetime.datetime.now()
    args = (current_time, phone)
    with connection.cursor() as cursor:
        cursor.execute(sql, args)
        connection.commit()
    return


def find_user_is_voted(phone):
    sql = "SELECT is_voted FROM t_user_base WHERE mobile = %s"
    args = (phone,)
    with connection.cursor() as cursor:
        cursor.execute(sql, args)
        row = cursor.fetchone()
    return row[0]


def insert_user_message(phone, message):
    current_time = datetime.datetime.now()
    sql = '''INSERT INTO t_user_message(mobile, message, create_time, type) values(%s, %s, %s, 2) '''
    args = (phone, message, current_time)
    with connection.cursor() as cursor:
        cursor.execute(sql, args)
        connection.commit()
    return