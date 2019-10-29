"""
Program: student.py
Author: Wes Brown
Last date modified: 10/28/19

Purpose: Create the class for Student
"""


def _valid_GPA(gpa):
    MAX_GPA = 4.0
    MIN_GPA = 0.0

    return MAX_GPA >= gpa >= MIN_GPA


def _valid_noun(name):
    name_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'-")
    return name_characters.issuperset(name)


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
        if _valid_noun(value):
            self._lname = value.issupperset
        else:
            raise ValueError

    @property
    def fname(self):
        return self._fname

    @fname.setter
    def fname(self, value):
        if _valid_noun(value):
            self._fname = value
        else:
            raise ValueError

    @property
    def major(self):
        return self._major

    @major.setter
    def major(self, value):
        if _valid_noun(value):
            self._major = value
        else:
            raise ValueError

    @property
    def gpa(self):
        return self._gpa

    @gpa.setter
    def gpa(self, value):
        if _valid_GPA(value):
            self._gpa = value
        else:
            raise ValueError

    def __str__(self) -> str:
        return self.lname + ", " + self.fname + " has major " + self.major + "with gpa: " + str(self.gpa)

    def __repr__(self) -> str:
        return self.__str__()
