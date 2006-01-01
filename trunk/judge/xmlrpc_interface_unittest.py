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
                            'output': '3\n7\n11', 'type': 'exact'}
        print 'Adding sample problem 1'
        # This proxy callRemote/deferred stuff is a bit weird.
        x = judge_connection.callRemote('add_problem', sample_problem_1)
        self.assertTrue(unittest.deferredResult(x))

        correct_submission = {'code': """import sys
        for line in sys.stdin:
           x, y = int(line.split()[0]), int(line.split()[1])
           print x + y"""}
        x = judge_connection.callRemote(correct_submission)
        self.assertTrue(unittest.deferredResult(x))

if __name__ == '__main__':
    #assert False, "the unittest doesn't actually run"
    twisted.trial.unittest.main()
