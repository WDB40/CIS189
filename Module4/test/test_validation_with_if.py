"""
Program: test_validations_with_if.py (validations_with_if.py)
Author: Wes Brown
Last date modified: 09/16/19

Purpose: To test the averaging of 3 scores.
"""

import unittest
from Module4.src.validation_with_if import average


class MyTestCase(unittest.TestCase):

    def test_average(self):
        self.assertEqual(90, average(85, 90, 95))

    def test_average_again(self):
        self.assertEqual(77, average(77, 77, 77))

    def test_invalid_input(self):
        self.assertEqual(-1, average(-80, 80, 80))

if __name__ == '__main__':
    unittest.main()
