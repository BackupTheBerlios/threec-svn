from sqlobject import *
from turbogears.database import AutoConnectHub

hub = AutoConnectHub()

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
    user = ForeignKey('User') #the creator

class Problem(SQLObject):
    '''Each problem gets an entry in here'''
    _connection = hub
    author = StringCol(notNone=True)
    problemName = StringCol(notNone=True,unique=True)
    problemUrl = StringCol(default='/searchProblems')
    timelimit = IntCol(default=10)
    memlimit = IntCol(default=512)
    correctness = IntCol(default=100)
    contest = ForeignKey('Contest')
    altjudgerprogram = StringCol(default=None)
    submissions = MultipleJoin('Submission')

class Submission(SQLObject):
    '''I think it would be better to just log all submissions which contests can store the ID to'''
    _connection = hub
    user = ForeignKey('User')
    problem = ForeignKey('Problem')
    code = StringCol(notNone=True)
    response = StringCol(length=10)
    speed = IntCol(notNone=True)
    memory = IntCol(notNone=True)
    time = DateTimeCol(default=DateTimeCol.now())
    contest = ForeignKey('Contest')
    language = StringCol(length=6)

class Page(SQLObject):
    '''Intended to hold wiki data - No idea if we want/need this'''
    _connection = hub
    pagename = StringCol(alternateID=True,length=40)
    data = StringCol()

