"""
Program: test_string_functions.py (string_functions.py)
Author: Wes Brown
Last date modified: 10/01/19

Purpose: Testing functions related to string and manipulating them.
"""

from Module6.src.string_functions import multiply_string

import unittest


class MyTestCase(unittest.TestCase):
    def test_multiply_string(self):
        self.assertEqual(multiply_string("Ayah", 5), "AyahAyahAyahAyahAyah")


if __name__ == '__main__':
    unittest.main()
