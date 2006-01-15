#!/usr/bin/python

import xmlrpc_interface

import twisted.trial.unittest
import twisted.internet.reactor
import twisted.web.server
import twisted.web.xmlrpc

class XMLRPCInterfaceTestCase(twisted.trial.unittest.TestCase):
    
    def setUp(self):
        # This setUp twisted stuff is just to start the server, ordinarily
        # the server would be already running, so you don't have to do this.
        xml_judger = xmlrpc_interface.XMLRPCJudgeInterface()
        xml_judger_site = twisted.web.server.Site(xml_judger)
        self.server = twisted.internet.reactor.listenTCP(
            0, xml_judger_site, interface = '127.0.0.1')
            
        self.port = self.server.getHost().port
                                           
    def tearDown(self):
        self.server.stopListening()
        # I just copied this from twisted/web/test/test_xmlrpc.py...
        # I don't know why the server iterates...
        twisted.internet.reactor.iterate()
        twisted.internet.reactor.iterate()

    def testAddProblems(self):
        print 'Connecting to server...',
        server_uri = "http://localhost:%d" % self.port
        judge_connection = twisted.web.xmlrpc.Proxy(server_uri)
        print 'Connected'
        sample_problem_1 = {'problem_number': 1, 'input': '1 2\n3 4\n5 6\n',
                            'output': '3\n7\n11\n', 'type': 'exact'}
        print 'Adding sample problem 1'
        # This proxy callRemote/deferred stuff is a bit weird.
        x = judge_connection.callRemote('add_problem', sample_problem_1)
        self.failUnless(twisted.trial.unittest.deferredResult(x))

        correct_submission = {'code': "import sys\n"
                              "for line in sys.stdin:\n"
                              "     tokens = line.split()\n"
                              "     x, y = int(tokens[0]), int(tokens[1])\n"
                              "     print x + y\n",
                              'problem_number': 1,
                              }
        x = judge_connection.callRemote('judge', correct_submission)
        self.failUnless(twisted.trial.unittest.deferredResult(x))

if __name__ == '__main__':
    import os
    import sys
    # The twisted guys are nuts, I can't figure out how to just run a test
    # directly from the command line (eg, ./my_unittest.py should run
    # the testing suite in my_unittest.  I can't figure out how to.  Boggle.
    os.system('trial ' + sys.argv[0])  
