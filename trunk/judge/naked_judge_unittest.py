#!/usr/bin/python

import os
import unittest
import naked_judge

class NakedJudgeTestCase(unittest.TestCase):
    def setUp(self):
        if os.getuid() == 0:
            # We are root, we can use security measures such as chroot,
            # so insecurity is not allowed.
            self.judger = naked_judge.NakedJudge(allow_insecurity = False)
        else:
            # We don't have the capabilities to do fancy things, run
            # insecurely
            self.judger = naked_judge.NakedJudge(allow_insecurity = True)
        
    def testAccepted(self):
        self.assertTrue(self.judger.judge_exact('echo 1', '1\n'))
        self.assertFalse(self.judger.judge_exact('echo 1', '\n'))
        # Since the command passed to judge exact won't do any shell magic,
        # we fudge a sleep x && echo 10 by writing a short inline python
        # program.
        waiter_template_program = '"import time\n' + \
                                  'start = time.time()\n' + \
                                  'while time.time() - start < %d: pass\n' + \
                                  'print 10\n"'

        prints_10_quickly = 'python -c ' + (waiter_template_program % 0)
        prints_10_slowly = 'python -c ' + (waiter_template_program % 2)
        self.assertTrue(self.judger.judge_exact(prints_10_quickly, '10\n'))
        # The second call should timeout.
        self.assertFalse(self.judger.judge_exact(prints_10_slowly, '10\n'))

    def testSplitArglist(self):
        input_output = [('echo', ['echo']),
                        ('echo 1', ['echo', '1']),
                        ('echo "hi"', ['echo', 'hi']),
                        ('echo "hello 1 2 3"', ['echo', 'hello 1 2 3']),
                        ('echo "hello    1    2 3"', ['echo', 'hello 1 2 3'])]
        for in_val, out_val in input_output:
            self.assertEquals(self.judger._split_arglist(in_val), out_val)


if __name__ == "__main__":
    unittest.main()
