from pymysql import cursors
from decoratorDB import getCursor


@getCursor
def saveSite(cursor: cursors.Cursor):
    pass


@getCursor
def selectSite(cursor: cursors.Cursor):
    pass


@getCursor
def selectObject(cursor: cursors.Cursor):
    pass
