import turbogears
import sqlobject
from dataobjects import User

class Search:
    @turbogears.expose(html='ccubed.templates.search')
    def index(self,user):
	person = User.byName(user)
