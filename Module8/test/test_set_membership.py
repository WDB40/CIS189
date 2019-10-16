"""
Program: test_set_membership.py (set_membership.py)
Author: Wes Brown
Last date modified: 10/15/19

Purpose: Test working with sets in Python
"""


import unittest
from Module8.src.set_membership import *


class MyTestCase(unittest.TestCase):
    def test_in_set_true(self):
        self.assertEqual(True, in_set({1, 2, 3, 4, 5}, 3))

    def test_in_set_false(self):
        self.assertEqual(False, in_set({1, 2, 3, 4, 5}, 6))


if __name__ == '__main__':
    unittest.main()
