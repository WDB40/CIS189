"""
Program: test_filename_validator.py
Author: Wes Brown
Last date modified: 12/08/19

Purpose: Testing that the filename_validator works properly
"""


import unittest
from FinalProject.src.validators.filename_validator import FilenameValidator


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.validator = FilenameValidator()

    def test_contains_numbers(self):
        self.validator.validate("123")
        self.assertFalse(self.validator.valid)

    def test_empty(self):
        self.validator.validate("")
        self.assertFalse(self.validator.valid)

    def test_valid(self):
        self.validator.validate("validName")
        self.assertTrue(self.validator.valid)


if __name__ == '__main__':
    unittest.main()
