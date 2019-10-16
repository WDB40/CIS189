"""
Program: test_assign_average.py (assign_average.py)
Author: Wes Brown
Last date modified: 10/15/19

Purpose: Test using dictionaries to implement a switch-esque statement
"""


import unittest
from Module8.src.assign_average import *


class MyTestCase(unittest.TestCase):
    def test_return_A(self):
        self.assertEqual(switch_average("A"), 90)

    def test_return_a(self):
        self.assertEqual(switch_average("a"), 90)

    def test_return_B(self):
        self.assertEqual(switch_average("B"), 80)

    def test_return_b(self):
        self.assertEqual(switch_average("b"), 80)

    def test_return_C(self):
        self.assertEqual(switch_average("C"), 70)

    def test_return_c(self):
        self.assertEqual(switch_average("c"), 70)

    def test_return_D(self):
        self.assertEqual(switch_average("D"), 60)

    def test_return_F(self):
        self.assertEqual(switch_average("F"), 50)

    def test_key_not_found(self):
        self.assertEqual(switch_average("g"), -1)


if __name__ == '__main__':
    unittest.main()
