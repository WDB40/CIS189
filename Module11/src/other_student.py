"""
Program: student.py
Author: Wes Brown
Last date modified: 11/04/19

Purpose: Create the class for student that has a person
"""


from Module11.src.person import Person


class Student:
    def __init__(self, student_id, person, major="Computer Science", gpa=0.0):
        self.student_id = student_id
        self.person = person
        self.major = major
        self.gpa = gpa

    @property
    def student_id(self):
        return self._student_id

    @student_id.setter
    def student_id(self, value):
        self._student_id = value

    @property
    def person(self):
        return self._person

    @person.setter
    def person(self, value):
        self._person = value

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

    def display(self):
        return "First Name: %s; Last Name: %s; Address: %s; Student ID: %s; Major: %s; GPA: %.2f" % (self.person.fname, self.person.lname, self.person.address, self.student_id, self.major, self.gpa)
