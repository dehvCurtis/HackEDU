import jwt
import pymysql


class LoggedOutException(Exception):
    '''Raising a LoggedOutException will redirect the user to the login screen
    in the app.
    '''
    pass

def account_lookup(account_id, jwt_token):
    try:
        token = jwt.decode(jwt_token, 'luBEK(P$x[%ZeQ4HAD5Ji1Z*;0Gcz583yP!v|KCmNEDDmQF/9P)>GpJK>Cx}3;R', algorithm='HS256')
    except Exception as e:
        raise LoggedOutException('User is not logged in')

    if "logged_in" in token.keys() and token["logged_in"] == True:
        conn = pymysql.connect(
            host='mysql',
            port=3306,
            user='root',
            passwd='letmein',
            db='BankApp'
        )
        cursor = conn.cursor()

        statement = "SELECT username FROM tbl_user WHERE id = " + account_id + ";"
        cursor.execute(statement)
        username_results = cursor.fetchone()

        if username_results:
            username = username_results[0]
            if username == token['username']:

                statement = "SELECT balance, dob FROM tbl_account WHERE user_id = " + account_id + ";"
                cursor.execute(statement)
                account_results = cursor.fetchone()

                conn.commit()
                cursor.close()
                conn.close()

                return {
                    'balance': account_results[0],
                    'dob': account_results[1],
                    'username': username
                }
        else:
            raise Exception('Account not found')
    else:
        raise LoggedOutException('User is not logged in')
