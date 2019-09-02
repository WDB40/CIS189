"""
Program: test_functions.py (camper_age_input.py)
Author: Wes Brown
Last date modified: 09/02/19

Purpose: To create, test, and use a function with python.
"""


import unittest

from Module2.src.camper_age_input import convert_to_months


class MyTestCase(unittest.TestCase):
    def test_5_years(self):
        self.assertEqual(5, convert_to_months(60))

    def test_10_years(self):
        self.assertEqual(4.5, convert_to_months(54))


if __name__ == '__main__':
    unittest.main()
