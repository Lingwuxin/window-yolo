import pymysql
from pymysql import cursors

mysql_user = {"host": "127.0.0.1", "user": "yolo_garbage_window", "password": "123456"}


def connectDB(useConnectionFunc):
    def connection(*args, **kwargs) -> pymysql.connections.Connection:
        connect = pymysql.connect(
            host=mysql_user["host"],
            user=mysql_user["user"],
            password=mysql_user["password"],
        )
        useConnectionFunc(connect)
        connect.close()

    return connection


def getCursor(useCursorFunc) -> cursors.Cursor:
    def newCursor(*args,**kwargs):
        connect = pymysql.connect(
            host=mysql_user["host"],
            user=mysql_user["user"],
            password=mysql_user["password"],
        )
        useCursorFunc(connect.cursor())
        connect.close()
    return newCursor

