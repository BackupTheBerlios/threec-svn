#!/usr/bin/python

import unittest
import naked_judge

class NakedJudgeTestCase(unittest.TestCase):
    def setUp(self):
        self.judger = naked_judge.NakedJudge()
        
    def testAccepted(self):
        ret = self.judger.judge_exact('echo 1', '\n')
        

if __name__ == "__main__":
    unittest.main()
