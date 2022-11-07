from decoratorDB import getCursor


@getCursor
def saveSite(*args, **kwargs):
    if "connect" not in kwargs:
        print("数据库连接异常")


@getCursor
def selectSite(*args, **kwargs):
    if "connect" not in kwargs:
        print("数据库连接异常")


@getCursor
def selectObject(*args, **kwargs):
    if "connect" not in kwargs:
        print("数据库连接异常")
