"""
Program: test_half_birthday.py (half_birthday.py)
Author: Wes Brown
Last date modified: 10/15/19

Purpose: Test using datetime to calculate a half-birthday
"""

import unittest
from datetime import datetime
from Module8.src.half_birthday import *


class MyTestCase(unittest.TestCase):
    def test_half_birthday(self):
        self.assertEqual(half_birthday(datetime(2019, 5, 10)), datetime(2019, 11, 10))

    def test_half_birthday_2(self):
        self.assertEqual(half_birthday(datetime(2019, 12, 10)), datetime(2020, 6, 10))

    def test_half_birthday_3(self):
        self.assertEqual(half_birthday(datetime(2019, 1, 10)), datetime(2019, 7, 10))


if __name__ == '__main__':
    unittest.main()
