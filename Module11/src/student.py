"""
Program: student.py
Author: Wes Brown
Last date modified: 10/29/19

Purpose: Create the class for student
"""


from Module11.src.person import Person


class Student(Person):
    def __init__(self, student_id, fname, lname, major="Computer Science", gpa=0.0, address=""):
        super().__init__(lname, fname, address)
        self.student_id = student_id
        self.major = major
        self.gpa = gpa

    @property
    def student_id(self):
        return self._student_id

    @student_id.setter
    def student_id(self, value):
        self._student_id = value

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
        return super().display() + f": ({self.student_id}) {self.major} GPA: {self.gpa}"
