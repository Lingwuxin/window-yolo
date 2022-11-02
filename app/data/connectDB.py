import pymysql
from pymysql import cursors


def contect_database(func):
    def wrapper():
        connect = pymysql.connect(
            host="127.0.0.1", user="yolo_garbage_window", password="123456"
        )
        cursor = connect.cursor()
        res = func(cursor)
        connect.close()
        return res

    return wrapper


@contect_database
def save_site(cursor: cursors.Cursor):
    pass


@contect_database
def select_site(cursor: cursors.Cursor):
    pass

@contect_database
def select_object(cursor:cursors.Cursor):
    pass