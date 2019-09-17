"""
Program: test_validations_with_try.py (validations_with_try.py)
Author: Wes Brown
Last date modified: 09/16/19

Purpose: To test the averaging of 3 scores with exceptions.
"""

import unittest
from Module4.src.validation_with_try import average


class MyTestCase(unittest.TestCase):

    def test_average(self):
        self.assertEqual(90, average(85, 90, 95))

    def test_average_again(self):
        self.assertEqual(77, average(77, 77, 77))

    def test_first_invalid_input(self):
        with self.assertRaises(ValueError):
            average(-1, 90, 90)

    def test_second_invalid_input(self):
        with self.assertRaises(ValueError):
            average(90, -1, 90)




if __name__ == '__main__':
    unittest.main()
