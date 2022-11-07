from decoratorDB import connectDB, getCursor
import mysql.connector


class DtabaseInit:
    def __init__(self) -> None:
        self.statue_code = 0
        try:
            mysql_user = {"host": "127.0.0.1", "user": "root", "password": "123456"}
            self.connect: mysql.connector.connection_cext.CMySQLConnection = (
                mysql.connector.connect(
                    host=mysql_user["host"],
                    user=mysql_user["user"],
                    password=mysql_user["password"],
                    auth_plugin="mysql_native_password",
                )
            )
            self.cursor = self.connect.cursor()
            with open("data/init.sql", "r") as sql:
                self.cursor.execute(sql.read())

        except Exception as e:
            print(e)
            self.statue_code = 400
        finally:
            if self.statue_code == 0:
                self.cursor.close()
                self.connect.close()
                print("数据库初始化成功")
            if self.statue_code != 0:
                print("数据库初始化失败")


a = DtabaseInit()
