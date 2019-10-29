"""
Program: test_student.py (student.py)
Author: Wes Brown
Last date modified: 10/28/19

Purpose: Test the class for Student
"""

import unittest
from Module10.src.student import Student


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.student = Student("Brown", "Wes", "CIS")

    def tearDown(self):
        del self.student

    def test_something(self):
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
