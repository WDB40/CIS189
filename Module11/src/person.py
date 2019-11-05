"""
Program: person.py
Author: Wes Brown
Last date modified: 10/29/19

Purpose: Create the class for person
"""


class Person:
    def __init__(self, lname, fname, address=""):
        self.lname = lname
        self.fname = fname
        self.address = address

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
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value

    def display(self):
        return f"{self.lname}, {self.fname}"
