#!/usr/bin/env python3
"""
Unit test cases for nodict.py
Students should not need to modify this file.
"""

__author__ = "madarp"

import sys
import unittest
import importlib
import inspect

# suppress __pycache__ and .pyc files
sys.dont_write_bytecode = True

# devs: change this to soln.nodict to test solution
PKG_NAME = 'nodict'


class TestNoDict(unittest.TestCase):
    """Main test fixture for nodict module"""
    pass


if __name__ == '__main__':
    unittest.main()
