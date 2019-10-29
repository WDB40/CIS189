"""
Program: test_student.py (student.py)
Author: Wes Brown
Last date modified: 10/28/19

Purpose: Test the class for Student
"""

import unittest
from Module10.src.student import Student


class MyTestCase(unittest.TestCase):
    LNAME = "Brown"
    FNAME = "Wes"
    MAJOR = "CIS"

    def setUp(self):
        self.LNAME = "Brown"
        self.FNAME = "Wes"
        self.MAJOR = "CIS"
        self.GPA = 0.0
        self.student = Student(self.LNAME, self.FNAME, self.MAJOR)

    def tearDown(self):
        del self.student

    def test_object_created_required_attributes(self):
        assert self.student.lname == self.LNAME
        assert self.student.fname == self.FNAME
        assert self.student.major == self.MAJOR
        assert self.student.gpa == self.GPA

    def test_object_created_all_attributes(self):
        this_gpa = 4.0
        this_student = Student(self.LNAME, self.FNAME, self.MAJOR, this_gpa)
        assert this_student.lname == self.LNAME
        assert this_student.fname == self.FNAME
        assert this_student.major == self.MAJOR
        assert this_student.gpa == this_gpa

    def test_object_not_created_error_last_name(self):
        with self.assertRaises(TypeError):
            this_student = Student(self.FNAME, self.MAJOR)


if __name__ == '__main__':
    unittest.main()
