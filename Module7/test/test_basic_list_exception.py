"""
Program: test_basic_list_exception.py (basic_list_exception.py)
Author: Wes Brown
Last date modified: 10/01/19

Purpose: Test working with exceptions with lists in python
"""


import unittest
from unittest.mock import patch
from Module7.src.basic_list_exception import *


class MyTestCase(unittest.TestCase):
    @patch('Module7.src.basic_list_exception.get_input', return_value=10)
    def test_make_list(self, input):
        self.assertEqual(make_list(), [10, 10, 10])

    @patch('Module7.src.basic_list_exception.get_input', return_value=15)
    def test_make_list_2(self, input):
        self.assertEqual(make_list(), [15, 15, 15])

    @patch('Module7.src.basic_list_exception.get_input', return_value=20)
    def test_make_list_3(self, input):
        self.assertEqual(make_list(), [20, 20, 20])

    @patch('Module7.src.basic_list_exception.get_input', return_value='Wes')
    def test_make_list_non_numeric(self, input):
        with self.assertRaises(ValueError):
            make_list()

    @patch('Module7.src.basic_list_exception.get_input', return_value=55)
    def test_make_list_above_range(self, input):
        with self.assertRaises(ValueError):
            make_list()

    @patch('Module7.src.basic_list_exception.get_input', return_value=0)
    def test_make_list_below_range(self, input):
        with self.assertRaises(ValueError):
            make_list()



if __name__ == '__main__':
    unittest.main()
