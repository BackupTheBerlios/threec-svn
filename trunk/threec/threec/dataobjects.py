from sqlobject import *
from turbogears.database import AutoConnectHub

hub = AutoConnectHub()

class User(SQLObject):
    _connection = hub
    user = StringCol(alternateID=True,length=15)
    email = StringCol(length=40)
    passwd = StringCol(length=40)
    
class Contest(SQLObject):
    _connection = hub
    start = DateTimeCol()
    end = DateTimeCol()
    name = StringCol(length=20)
    problemset = IntCol()

class Problems(SQLObject):
    _connection = hub
    problem = IntCol()
    problemset = IntCol()
    problemstmt = StringCol()
    timelimit = IntCol()
    memlimit = IntCol()
    correctness = IntCol()
    altjudgerprogram = StringCol(default=None)

class Page(SQLObject):
    _connection = hub
    pagename = StringCol(alternateID=True,length=40)
    data = StringCol()
