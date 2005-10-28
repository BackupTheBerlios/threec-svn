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
    contests_hosting = MultipleJoin('Contest')
    submissions = MultipleJoin('Submission')
    
class Contest(SQLObject):
    '''The basic data for each individual contest - Non-contest times are really a special case contest?'''
    _connection = hub
    start = DateTimeCol()
    end = DateTimeCol()
    name = StringCol(length=20)
    problemset = MultipleJoin('Problem')
    submission = MultipleJoin('Submission')
    creator = StringCol()

class Problem(SQLObject):
    '''Each problem gets an entry in here'''
    _connection = hub
    author = StringCol()
    problemName = StringCol()
    problemUrl = StringCol()
    timelimit = IntCol()
    memlimit = IntCol()
    correctness = IntCol()
    altjudgerprogram = StringCol(default=None)

class Submission(SQLObject):
    '''I think it would be better to just log all submissions which contests can store the ID to'''
    user = ForeignKey('User')
    problem = ForeignKey('Problem')
    code = StringCol()
    response = StringCol(length=10)
    speed = IntCol()
    memory = IntCol()
    time = DateTimeCol()
    contest = ForeignKey('Contest')

class Page(SQLObject):
    '''Intended to hold wiki data - No idea if we want/need this'''
    _connection = hub
    pagename = StringCol(alternateID=True,length=40)
    data = StringCol()

