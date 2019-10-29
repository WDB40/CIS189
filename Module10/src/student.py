"""
Program: student.py
Author: Wes Brown
Last date modified: 10/28/19

Purpose: Create the class for Student
"""


class Student:

    def __init__(self, lname, fname, major, gpa=0.0):
        self.lname = lname
        self.fname = fname
        self.major = major
        self.gpa = gpa

    @property
    def lname(self):
        return self._lname

    @lname.setter
    def lname(self, value):
        self._lname = value

    @property
    def fname(self):
        return self._fname

    @fname.setter
    def fname(self, value):
        self._fname = value

    @property
    def major(self):
        return self._major

    @major.setter
    def major(self, value):
        self._major = value

    @property
    def gpa(self):
        return self._gpa

    @gpa.setter
    def gpa(self, value):
        self._gpa = value

    def __str__(self) -> str:
        return self.lname + ", " + self.fname + " has major " + self.major + "with gpa: " + str(self.gpa)

    def __repr__(self) -> str:
        return self.__str__()
