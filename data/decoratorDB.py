import mysql.connector

mysql_user = {
    "host": "127.0.0.1",
    "user": "yolo_user",
    "password": "yologarbage33214",
    "database": "YOLO",
}


def connectDB(useConnectionFunc):
    def connection(*args, **kwargs):
        try:
            connect: mysql.connector.connection_cext.CMySQLConnection = (
                mysql.connector.connect(
                    host=mysql_user["host"],
                    user=mysql_user["user"],
                    password=mysql_user["password"],
                    auth_plugin="mysql_native_password",
                )
            )
            kwargs["connect"] = connect
            kwargs["cursor"] = connect.cursor()
            useConnectionFunc(*args, **kwargs)
        except Exception as e:
            print(e)
        finally:
            connect.close()

    return connection
