import mysql.connector

mysql_user = {"host": "127.0.0.1", "user": "yolo_user", "password": "yologarbage33214","database":"YOLO"}

def connectDB(useConnectionFunc):
    def connection(*args, **kwargs) -> mysql.connector:
        connect = mysql.connector.connect(
            host=mysql_user["host"],
            user=mysql_user["user"],
            password=mysql_user["password"],
            database=mysql_user
        )
        useConnectionFunc(connect)
        connect.close()

    return connection


def getCursor(useCursorFunc) :
    def newCursor(*args,**kwargs):
        connect = mysql.connector.connect(
            host=mysql_user["host"],
            user=mysql_user["user"],
            password=mysql_user["password"],
        )
        kwargs['cursor']=connect.cursor()
        useCursorFunc(*args,**kwargs)
        connect.close()
    return newCursor

