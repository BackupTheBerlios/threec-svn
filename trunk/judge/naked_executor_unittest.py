#!/usr/bin/python

import os
import unittest
import naked_executor

class NakedExecutorTestCase(unittest.TestCase):
    def setUp(self):
        if os.getuid() == 0:
            # We are root, we can use security measures such as chroot,
            # so insecurity is not allowed.
            self.executor = naked_executor.NakedExecutor(
                allow_insecurity = False)
        else:
            # We don't have the capabilities to do fancy things, run
            # insecurely
            self.executor = naked_executor.NakedExecutor(
                allow_insecurity = True)
        
    def testCaptureStdout(self):
        self.assertEquals(self.executor.capture_stdout('echo 1'), '1\n')
        # Since the command passed to judge exact won't do any shell magic,
        # we fudge a sleep x && echo 10 by writing a short inline python
        # program.
        waiter_template_program = '"import time\n' + \
                                  'start = time.time()\n' + \
                                  'while time.time() - start < %d: pass\n' + \
                                  'print 10\n"'

        print_10_quick = 'python -c ' + (waiter_template_program % 0)
        print_10_slow = 'python -c ' + (waiter_template_program % 2)
        self.assertEquals(self.executor.capture_stdout(print_10_quick), '10\n')
        # The second call should timeout.
        self.assertEquals(self.executor.capture_stdout(print_10_slow), '')

    def testSplitArglist(self):
        input_output = [
            ('echo', ['echo']),
            ('echo 1', ['echo', '1']),
            ('echo "hi"', ['echo', 'hi']),
            ('echo "hello 1 2 3"', ['echo', 'hello 1 2 3']),
            ('echo "hello    1    2 3"', ['echo', 'hello 1 2 3']),
            ('some "quoted stuff" more  "quoted   stuff"',
             ['some', 'quoted stuff', 'more', 'quoted stuff'])
            ]
        
        for in_val, out_val in input_output:
            self.assertEquals(self.executor._split_arglist(in_val), out_val)


if __name__ == "__main__":
    unittest.main()
