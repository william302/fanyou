from django.db import connection


def find_user(phone):
    sql = "SELECT merchant_id FROM t_user_base WHERE mobile = %s"
    args = (phone,)
    with connection.cursor() as cursor:
        cursor.execute(sql, args)
        row = cursor.fetchone()
    return row


def insert_user(phone, dealer_id):
    sql = '''INSERT INTO t_user_base(mobile, merchant_id) VALUES(%s, %s)'''
    args = [phone, dealer_id]
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
