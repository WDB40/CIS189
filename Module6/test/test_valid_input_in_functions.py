"""
Program: test_validate_input_in_functions.py (validate_input_in_functions.py)
Author: Wes Brown
Last date modified: 10/01/19

Purpose: Take score input and validate the score.
"""


import unittest
from Module6.src.validate_input_in_functions import score_input


class MyTestCase(unittest.TestCase):
    def test_score_input_test_name(self):
        self.assertEqual(score_input("Test Name"), "Test Name: 0")

    def test_score_input_score_valid(self):
        self.assertEqual(score_input("Test Name", 80), "Test Name: 80")

    def test_score_input_score_below_range(self):
        self.assertEqual(score_input("Test Name", -1), "Invalid test score, try again!")

    def test_score_input_score_above_range(self):
        self.assertEqual(score_input("Test Name", 101), "Invalid test score, try again!")

    def test_score_input_score_non_numeric(self):
        self.assertEqual(score_input("Test Name", "abc"), "Invalid test score, try again!")

    def test_score_input_invalid_message(self):
        self.assertEqual(score_input("Test Name", 101, "That's not right!"), "That's not right!")


if __name__ == '__main__':
    unittest.main()
