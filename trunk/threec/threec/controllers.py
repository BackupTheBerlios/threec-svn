import turbogears
from model import Page,hub,User
from sqlobject import SQLObjectNotFound
import cherrypy
import sha

class Root:

    @turbogears.expose(html="threec.templates.homepage")
    def index(self,unknown=False):
	ret = {}
	if unknown:
	    message = ['Unknown username/password']
	    ret['message']=message
	    
	return ret

    @turbogears.expose(html='threec.templates.edit')
    def edit(self,pagename,new=False):
	if not new:
	    page = Page.byPagename(pagename)
	    pagename = page.pagename
	    data = page.data
	else:
	    pagename = pagename
	    data = 'Edit me please'
	return dict(pagename=pagename,data=data)

    @turbogears.expose(html='threec.templates.userList')
    def searchuser(self,user,type):
	if type is 'coder':
	    type = 'Coder'
	else:
	    type = 'Problem Setter'
	return {'user':user,'type':type}

    def save(self,pagename,data,submit):
	hub.begin()
	page = Page.byPagename(pagename)
	page.data = data
	hub.commit()
	hub.end()
	turbogears.flash("Changes saved!")
	raise cherrypy.HTTPRedirect('/%s'%pagename)

    @turbogears.expose(html='threec.templates.createuser')
    def createuser(self,**kw):
	return kw

    @turbogears.expose(html='threec.templates.createuser')
    def createaccount(self,**kw):
	#ret = {'message':''}
	message = []
	ret = {'message':message}
	good = True

	for x in kw.items():
	    if len(x[1]) < 3:
		#ret[x[0]]=' %s must be at least 3 characters'%x[1]
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
    def confirm(self,passwdchk,email):
	return dict()

    @turbogears.expose(html='threec.templates.login')
    def login(self,user,passwd):
	try:
	    user = User.byUser(user)
	except SQLObjectNotFound:
	    raise cherrypy.HTTPRedirect('/createuser?')

	if sha.sha(passwd).hexdigest() == user.passwd:
	    #create a session
	    pass
	else:
	    raise cherrypy.HTTPRedirect('/index?unknown=true' % user)

	return 'Logged in successfully'

    #@turbogears.expose(html="threec.templates.homepage")
    #def searchuser(self,username="Unknown"):
	#return "I couldn't find %s in the database"%username
