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


if __name__ == "__main__":
    unittest.main()
