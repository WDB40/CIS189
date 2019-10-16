"""
Program: test_dict_membership.py (dict_membership.py)
Author: Wes Brown
Last date modified: 10/15/19

Purpose: Testing working with dictionaries in Python
"""


import unittest
from Module8.src.dict_membership import *


class MyTestCase(unittest.TestCase):
    def test_in_dict_true(self):
        self.assertEqual(True, in_dict({"A": 1, "B": 2, "C": 3, "D": 4, "E": 5}, "C"))

    def test_in_dict_false(self):
        self.assertEqual(False, in_dict({"A": 1, "B": 2, "C": 3, "D": 4, "E": 5}, "F"))


if __name__ == '__main__':
    unittest.main()
