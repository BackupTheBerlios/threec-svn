#!/usr/bin/env python
import pkg_resources
pkg_resources.require("TurboGears")

import cherrypy
from os.path import *

# look for setup.py in this directory. If it's not there, this script is
# probably installed
if exists(join(dirname(__file__), "setup.py")):
    cherrypy.config.update(file="dev.cfg")
else:
    cherrypy.config.update(file="prod.cfg")

from threec.controllers import Root

cherrypy.root = Root()
cherrypy.server.start()
