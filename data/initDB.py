import mysql.connector
import json
from typing import Dict


class DtabaseInit:
    def __init__(self) -> None:
        self.statue_code: int = 0
        self.root: Dict[str:str] = None
        self.user: Dict[str:str] = None
        try:
            with open("data/databaseUser.json") as js_file:
                user_s: Dict[str:str] = json.load(js_file)
                self.root = user_s["root"]
                self.user = user_s["user"]

        except Exception as e:
            print(e)
        self.init_Database()
        self.crete_DBtools_file()

    def init_Database(self):
        try:
            self.connect: mysql.connector.connection_cext.CMySQLConnection = (
                mysql.connector.connect(
                    host=self.root["host"],
                    user=self.root["name"],
                    password=self.root["password"],
                    auth_plugin="mysql_native_password",
                )
            )
            self.cursor = self.connect.cursor()
            self.cursor.execute(
                f"""
            begin;
            create database {self.user['database']};
            use {self.user['database']};
            CREATE TABLE yoloGarbage (
            num int primary key,
            garbage varchar(255),
            accuracy decimal(20,18),
            xywh_x decimal(20,18),
            xywh_y decimal(20,18),
            xywh_w decimal(20,18),
            xywh_h decimal(20,18),
            in_datetime datetime default CURRENT_TIMESTAMP on update CURRENT_TIMESTAMP
            );
            CREATE USER '{self.user['name']}'@'%' IDENTIFIED BY '{self.user['password']}';
            grant all privileges on YOLO.* to 'yolo_user'@'{self.user['host']}' with grant option;
            commit;
            """
            )

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

    def crete_DBtools_file(self):
        with open("data\decoratorDB.py", "w") as f:
            f.write(
                f"""
import mysql.connector


def connectDB(useConnectionFunc):
    def connection(*args, **kwargs):
        mysql_user = dict()
        mysql_user['name'] = '{self.user['name']}'
        mysql_user['host'] = '{self.user['host']}'
        mysql_user['password'] = '{self.user['password']}'
        try:
            connect: mysql.connector.connection_cext.CMySQLConnection = (
                mysql.connector.connect(
                    host=mysql_user["host"],
                    user=mysql_user["name"],
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
                """
            )


def main():
    database_init = DtabaseInit()


if __name__ == "__main__":
    main()
