"""
Program: average_score.py
Author: Wes Brown
Last date modified: 09/09/19

Purpose: To receive information about a student and then average 3 scores.
"""


def average():
    val1 = float(input("Enter the first score: "))
    val2 = float(input("Enter the second score: "))
    val3 = float(input("Enter the third score: "))

    return (val1 + val2 + val3) / 3


if __name__ == '__main__':
    last_name = input("What is the student's last name? ")
    first_name = input("What is the student's first name? ")
    age = int(input("What is the student's age? "))
    average_score = average()

    print("%s, %s age: %d average grade: %.2f" % (last_name, first_name, age, average_score))
