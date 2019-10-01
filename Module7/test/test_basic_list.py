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
    @patch('Module7.src.basic_list.get_input', return_value='5')
    def test_something(self):
        self.assertEqual(make_list(), [5, 5, 5])


if __name__ == '__main__':
    unittest.main()
