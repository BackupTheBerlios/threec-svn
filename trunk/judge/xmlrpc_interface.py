#!/usr/bin/python

import pprint
from twisted.web import xmlrpc, server

class XMLRPCJudgeInterface(xmlrpc.XMLRPC):
    """The XML Interface to the judger"""

    def xmlrpc_judge(self, submission):
        """Judge submission"""
        pprint.pprint(submission)
        problem_number = submission['problem_number']
        return True
    
    def xmlrpc_add_problem(self, problem_args):
        pprint.pprint(problem_args)
        if problem_args['type'] != 'exact':
            # Only exact judgers are supported at the moment.
            return False

        problem_number = problem_args["problem_number"]
        input, output = problem_args["input"], problem_args["output"]
        return True

if __name__ == '__main__':
    from twisted.internet import reactor
    r = XMLRPCJudgeInterface()
    reactor.listenTCP(7080, server.Site(r))
    reactor.run()
