# Non-Compliant Code
import os
import untangle
import pymysql

def parse_upload(xml_data):
    conn = pymysql.connect(
        host='xxe-mysql',
        port=3306,
        user='root',
        passwd='letmein',
        db='PhonebookApp'
    )
    cursor = conn.cursor(pymysql.cursors.DictCursor)

    data = untangle.parse(xml_data, feature_external_ges=True)

    search_results = list()
    for user in data.Users.User:
        cursor.execute("SELECT name, email, phone FROM tbl_user WHERE name LIKE '%" + user.Name.cdata + "%'")
        results = cursor.fetchall()
        if len(results) > 0:
            search_results.append({"name": user.Name.cdata, "results": results})
        else:
            search_results.append({"error": "No results found for {0}".format(user.Name.cdata)})

    conn.commit()
    cursor.close()
    conn.close()

    return search_results

# Compliant Code
import os
import untangle
import pymysql

def parse_upload(xml_data):
    conn = pymysql.connect(
        host='xxe-mysql',
        port=3306,
        user='root',
        passwd='letmein',
        db='PhonebookApp'
    )
    cursor = conn.cursor(pymysql.cursors.DictCursor)

    data = untangle.parse(xml_data, feature_external_ges=False)

    search_results = list()
    for user in data.Users.User:
        cursor.execute("SELECT name, email, phone FROM tbl_user WHERE name LIKE '%" + user.Name.cdata + "%'")
        results = cursor.fetchall()
        if len(results) > 0:
            search_results.append({"name": user.Name.cdata, "results": results})
        else:
            search_results.append({"error": "No results found for {0}".format(user.Name.cdata)})

    conn.commit()
    cursor.close()
    conn.close()

    return search_results
