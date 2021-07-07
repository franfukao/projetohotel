import pymysql.cursors


def connectBD():
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password='',
        database='dbprojetohotel',
        cursorclass=pymysql.cursors.DictCursor
    )
    return conn
