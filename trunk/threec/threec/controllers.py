import turbogears
from model import Page,hub,User,Contest,Submission,Problem
from sqlobject import SQLObjectNotFound
import cherrypy
import sha,datetime

def separateContests(contest):
    return [contest.name,contest.start,contest.end,contest.user.user,'/problems?contestId=%d'%contest.id]

def separateSubmission(subm):
    return [subm.problem.problemName,subm.problem.problemUrl,'/viewcode?submissionId=%d'%subm.id]

def separateProblems(prob):
    return [prob.problemName,prob.problemUrl,prob.author,prob.contest.name,'/problems?contestId=%d'%prob.contest.id,'/submissions?problemId=%d'%prob.id]

class Root:

    @turbogears.expose(html="threec.templates.homepage")
    def index(self,unknown=False):
	message = []
	ret = {'message':message}
	ret = {}
	if unknown:
	    message.append('Unknown username/password')
	    
	return ret

    @turbogears.expose(html='threec.templates.editcontest')
    def editcontest(self,contestId,user):
	name = ''
	start = ''
	end = ''
	problems = []
	ret = {'name':name,'start':start,'end':end,'problemset':problems,'user':user}

	if contestId:
	    contest = Contest.get(contestId)
	    name = contest.name
	    start = contest.start
	    end = contest.end
	    problems = contest.problemset

	return ret

    @turbogears.expose(html='threec.templates.hosting')
    def hostcontest(self,user=None,passwd=None):
	if not user:
	    return {'message':['Must enter a valid username and password to manage contests'],'tg_template':'threec.templates.homepage'}

	loginSuccessful = login(self,user,passwd)
	if loginSuccessful['message'][0].count('invalid'):
	    return {'message':['Must enter a valid username and password to manage contests'],'tg_template':'threec.templates.homepage'}

	user = User.byUser(user)
	priorContests = []
	upcomingContests = []
	now = datetime.datetime.now()
	for contest in user.contests_hosting:
	    if contest.start > now:
		upcomingContests.append(contest)
	    else:
		priorContests.append(contest)

	ret = {'prior':priorContests,'upcoming':upcomingContests,'tg_template':'threec.templates.managecontests','user':user}
	return ret

    @turbogears.expose(html='threec.templates.userlist')
    def searchusers(self,userName):
	message = []
	ret = {'message':message}
	try:
	    user = User.byUser(userName)
	except SQLObjectNotFound:
	    message.append('%s is an unknown username'%userName)
	    ret['tg_template'] = 'threec.templates.homepage'
	    return ret

	ret['user'] = userName
	submissions = [separateSubmission(q) for q in user.submissions]
	ret['submissions']=submissions
	return ret

    @turbogears.expose(html='threec.templates.viewcode')
    def viewcode(self,submissionId):
	message = []
	ret = {'message':message}

	try:
	    subm = Submission.get(submissionId)
	except SQLObjectNotFound:
	    message.append('%d is an unknown submission ID'%submissionId)
	    ret['tg_template']='threec.templates.homepage'
	    return ret
	
	#ret['code'] = subm.code
	#return ret
	return subm.code #kills < > thinking they are tags

    @turbogears.expose(html='threec.templates.homepage')
    def default(self,*args,**kw):
	#message = [str(kw)]
	#message.append(str(args))
	#ret = {'message':message}
	#return ret
	ret = {}

	print args[0]

	try:
	    if args[0] == 'problems':
		print 'good'
		ret['tg_template']='threec.templates.problemstatement'
		ret['problem']=Page.byPagename('%s_%s'%(args[1],args[2])).data
		return ret
	except IndexError:
	    return 'Something unintended happened'

    @turbogears.expose(html='threec.templates.createuser')
    def createuser(self,**kw):
	#message = []
	#kw['message']=message
	return dict()
    
    @turbogears.expose(html='threec.templates.author')
    def author(self,s):
	probs = Problem.select('author="%s"'%s)
	problems = []
	ret = {'problems':problems}
	now = datetime.datetime.now()
	for item in probs:
	    if item.contest.start < now:
		problems.append([item.problemName,item.problemUrl])
	    
	ret['author']=s
	return ret

    @turbogears.expose(html='threec.templates.contests')
    def upcomingcontests(self,**kw):
	contests = Contest.select()
	_contests = []
	now = datetime.datetime.now()
	for contest in contests:
	    if contest.start > now:
		_contests.append(separateContests(contest))

	if not len(_contests):
	    ret = {'message':['No contests are scheduled']};
	else:
	    ret = {}

	ret['contests']=_contests
	ret['showProblemSetLink']=False
	return ret

    @turbogears.expose(html='threec.templates.contests')
    def contests(self,**kw):
	contests = Contest.select()
	_contests = []
	now = datetime.datetime.now()
	for contest in contests:
	    if contest.start < now:
		_contests.append(separateContests(contest))
	    
	ret = {'contests':_contests,'showProblemSetLink':True}
	return ret

    @turbogears.expose(html='threec.templates.problems')
    def problems(self,contestId):
	problems = []
	ret = {'problems':problems}
	try:
	    contest = Contest.get(int(contestId))
	except SQLObjectNotFound:
	    ret['message'] = ['%d is not a valid contest id'%contestId]
	    return ret

	if contest.start > datetime.datetime.now():
	    ret['message'] = ['The contest has not started yet']
	    return ret

	set = contest.problemset
	for item in set:
	    problems.append([item.problemName,item.problemUrl,item.author])

	ret['message']=['Problem set for %s'%contest.name]
	return ret

    @turbogears.expose(html='threec.templates.createuser')
    def createaccount(self,**kw):
	message = []
	ret = {'message':message}
	good = True

	for x in kw.items():
	    if len(x[1]) < 3:
		message.append('%s must be at least 3 characters'%x[0])
		good = False

	if not good:
	    print str(ret)
	    return ret

	try:
	    user = User.byUser(kw['username'])
	except SQLObjectNotFound:
	    if not kw['passwd'] == kw['passwdchk']:
		print 'stupid people'
		message.append('You mistyped your password and/or its confirmation')
		return ret

	    hub.begin()
	    User(user=kw['username'],passwd=sha.sha(kw['passwd']).hexdigest(),email=kw['email'])
	    message.append('You have successfully created your account %s.  Try logging in now!' % kw['username'])
	    hub.commit()
	    hub.end()
	    ret['tg_template']='threec.templates.homepage'
	    print str(ret)
	    return ret

	message.append('That name is already taken please try again')
	return ret
	
    @turbogears.expose(html='threec.templates.homepage')
    def login(self,user,passwd):
	message = []
	ret = {'message':message}

	try:
	    user = User.byUser(user)
	except SQLObjectNotFound:
	    message.append('That is an invalid Username/Password')
	    return ret

	if sha.sha(passwd).hexdigest() == user.passwd:
	    #create a session
	    pass
	else:
	    message.append('That is an invalid Username/Password')
	    return ret

	message.append('You have successfully logged in')
	return ret

    #@turbogears.expose(html="threec.templates.homepage")
    #def searchuser(self,username="Unknown"):
	#return "I couldn't find %s in the database"%username
