"""
Program: test_basic_list.py (basic_list.py)
Author: Wes Brown
Last date modified: 10/01/19

Purpose: Test how we manipulate lists with python
"""


import unittest
from unittest.mock import patch
from Module7.src.basic_list import *


class MyTestCase(unittest.TestCase):
    @patch('Module7.src.basic_list.get_input', return_value=10)
    def test_make_list(self, input):
        self.assertEqual(make_list(), [10, 10, 10])


if __name__ == '__main__':
    unittest.main()
