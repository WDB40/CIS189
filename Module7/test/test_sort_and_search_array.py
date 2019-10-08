"""
Program: sort_and_search_array.py
Author: Wes Brown
Last date modified: 10/07/19

Purpose: Sorting and searching an array in python.
"""


import unittest
from Module7.src.sort_and_search_array import *


class MyTestCase(unittest.TestCase):
    def test_search_item_found(self):
        self.assertEqual(search_array([1, 2, 3, 4, 5], 3), 2)

    def test_search_item_not_found(self):
        self.assertEqual(search_array([1, 2, 3, 4, 5], 6), -1)

    def test_sort_array(self):
        self.assertEqual(sort_array([5, 1, 4, 2, 3]), [1, 2, 3, 4, 5])


if __name__ == '__main__':
    unittest.main()
