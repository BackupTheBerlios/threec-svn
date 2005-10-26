from sqlobject import *
from turbogears.database import AutoConnectHub

hub = AutoConnectHub()
'''I don't think these all need to have _connection = hub, I dont think we will be using a lot of
transactions'''

class User(SQLObject):
    '''Self explanatory'''
    _connection = hub
    user = StringCol(alternateID=True,length=15)
    email = StringCol(length=40)
    passwd = StringCol(length=40)
    
class Contest(SQLObject):
    '''The basic data for each individual contest - Non-contest times are really a special case contest?'''
    _connection = hub
    start = DateTimeCol()
    end = DateTimeCol()
    name = StringCol(length=20)
    problemset = IntCol()
    creator = StringCol()

class ContestLog(SQLObject):
    '''A contest is a series of submissions - Non-contest submissions is really just a special case contest?'''
    _connection = hub
    contestName = StringCol()
    submission = IntCol()

class ContestProblemMapping(SQLObject):
    '''Provides a mapping from contests to problems and vice versa.  Using the power of
    SQLObject that puts the objects in here for convenience'''
    contestName = StringCol(length=20)
    problemName = StringCol()
    def getContest(problem):
	pass
    
    def getProblems(contest):
	pass

class Problems(SQLObject):
    '''Each problem gets an entry in here'''
    _connection = hub
    author = StringCol()
    problemName = StringCol()
    problemUrl = StringCol()
    timelimit = IntCol()
    memlimit = IntCol()
    correctness = IntCol()
    altjudgerprogram = StringCol(default=None)

class Page(SQLObject):
    '''Intended to hold wiki data - No idea if we want/need this'''
    _connection = hub
    pagename = StringCol(alternateID=True,length=40)
    data = StringCol()

class Submission(SQLObject):
    '''I think it would be better to just log all submissions which contests can store the ID to'''
    user = StringCol(length=15)
    problem = IntCol()
    code = StringCol()
    response = StringCol(length=10)
    speed = IntCol()
    memory = IntCol()
    time = DateTimeCol()
