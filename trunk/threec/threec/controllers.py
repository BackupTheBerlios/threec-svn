import turbogears
from model import Page,hub,User,Contest,Submission,Problem
from sqlobject import SQLObjectNotFound
import cherrypy
import sha

class Root:

    @turbogears.expose(html="threec.templates.homepage")
    def index(self,unknown=False):
	message = []
	ret = {'message':message}
	ret = {}
	if unknown:
	    message.append('Unknown username/password')
	    
	return ret

    @turbogears.expose(html='threec.templates.homepage')
    def searchUsers(self,user):
	message = []
	try:
	    message.append(User.byUser(user))
	except SQLObjectNotFound:
	    message.append('%s not found'%user)
	ret = {'message':message}
	return ret

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
    
    @turbogears.expose(html='threec.templates.contests')
    def contests(self,**kw):
	contests = Contest.select()
	_contests = []
	for contest in contests:
	    _contests.append([contest.name,contest.start,contest.end,contest.user.user,'/problems?contest=%d'%contest.id])
	    
	ret = {'contests':_contests}
	return ret

    @turbogears.expose(html='threec.templates.problems')
    def problems(self,contest):
	problems = []
	ret = {'problems':problems}
	contest = Contest.get(int(contest))
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
