"""
Program: gui_driver.py
Author: Wes Brown
Last date modified: 10/29/19

Purpose: Test class for person and student
"""


from Module11.src.person import Person
from Module11.src.student import Student


if __name__ == '__main__':
    my_student = Student(900111111, 'Song', 'River')
    print(my_student.display())
    my_student = Student(900111111, 'Song', 'River', 'Computer Engineering')
    print(my_student.display())
    my_student = Student(900111111, 'Song', 'River', 'Computer Engineering', 4.0)
    print(my_student.display())

    del my_student
