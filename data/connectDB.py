from decoratorDB import connectDB
from PyQt5 import QtCore

@connectDB
def saveSite(connect,cursor,data=None):
    print(data)


@connectDB
def selectSite(connect,cursor):
    pass
