# SQL Injection: Part 1

# Non-Compliant Code
import os
import pymysql


def login(username, password):
    conn = pymysql.connect(host='db', port=3306, user='root', passwd='letmein', db='SocialMediaApp')
    cursor = conn.cursor()

    query = "SELECT * FROM users WHERE username = '" + username + "' AND password = '"+ password + "';"
    cursor.execute(query)
    data = cursor.fetchall()

    conn.commit()
    cursor.close()
    conn.close()

    if not data:
        return False

    return True


# Compliant Code
import os
import pymysql


def login(username, password):
    conn = pymysql.connect(host='db', port=3306, user='root', passwd='letmein', db='SocialMediaApp')
    cursor = conn.cursor()


    cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
    data = cursor.fetchall()

    conn.commit()
    cursor.close()
    conn.close()

    if not data:
        return False

    return True