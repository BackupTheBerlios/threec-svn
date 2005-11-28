#!/usr/bin/python

"""A file with judge logging configuration"""

import logging
import sys

_judge_logger = logging.getLogger('judge')
console = logging.StreamHandler()
console.setLevel(logging.ERROR)
# console.setLevel(logging.DEBUG) # uncomment for more verbose output
_judge_logger.addHandler(console)

