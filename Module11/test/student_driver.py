"""
Program: student_driver.py
Author: Wes Brown
Last date modified: 11/04/19

Purpose: Test class for the student that has a person
"""
from Module11.src.other_student import Student
from Module11.src.person import Person

if __name__ == '__main__':
    my_person = Person("Brown", "Wes", "111 Main Street")
    my_student = Student("123", my_person, "Industrial Engineering", 4.0)

    my_student.major = "Being Awesome!"
    my_student.gpa = 3.0

    print(my_student.display())
    del my_person
    del my_student
