#!/usr/bin/python

"""A file with judge logging configuration"""

import logging
import sys

_judge_logger = logging.getLogger('judge')
_judge_logger.setLevel(logging.ERROR)
assert not _judge_logger.isEnabledFor(logging.DEBUG)
_judge_logger.setLevel(logging.DEBUG) # uncomment for more verbose output
console = logging.StreamHandler()
_judge_logger.addHandler(console)
