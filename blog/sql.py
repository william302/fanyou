from django.db import connection


def find_user(phone):
    sql = "SELECT dealer_id FROM users WHERE phone = %s"
    args = (phone,)
    with connection.cursor() as cursor:
        cursor.execute(sql, args)
        row = cursor.fetchone()
    return row


def insert_user(phone, dealer_id):
    sql = '''INSERT INTO users(phone, dealer_id) VALUES(%s, %s)'''
    args = [phone, dealer_id]
    with connection.cursor() as cursor:
        cursor.execute(sql, args)
        connection.commit()
    return


def update_user(phone, dealer_id):
    sql = "update users set dealer_id = %s where phone = %s"
    args = [dealer_id, phone]
    with connection.cursor() as cursor:
        cursor.execute(sql, args)
        connection.commit()
    return