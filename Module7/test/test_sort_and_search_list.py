"""
Program: test_sort_and_search_list.py (sort_and_search_list.py)
Author: Wes Brown
Last date modified: 10/07/19

Purpose: Testing the sorting and searching a list in python.
"""


import unittest
from Module7.src.sort_and_search_list import *


class MyTestCase(unittest.TestCase):
    def test_search_item_found(self):
        self.assertEqual(search_list([1, 2, 3, 4], 3), 2)

    def test_search_item_not_found(self):
        self.assertEqual(search_list([1, 2, 3, 4], 5), -1)

    def test_sort_numbers(self):
        self.assertEqual(sort_list([5, 1, 4, 3, 2]), [1, 2, 3, 4, 5])

    def test_sort_alpha(self):
        self.assertEqual(sort_list(["e", "a", "d", "b", "c"]), ["a", "b", "c", "d", "e"])


if __name__ == '__main__':
    unittest.main()
