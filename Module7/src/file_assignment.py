"""
Program: file_assignment.py
Author: Wes Brown
Last date modified: 10/07/19

Purpose: Working with files in python
"""


import os


def write_to_file(write_items):
    file_dir = os.path.dirname(os.path.abspath(__file__))
    file_name = 'student_info.txt'

    try:

        with open(os.path.join(file_dir, file_name), "a") as write_file:
            for item in write_items:
                write_file.write(item)
                write_file.write(" ")

            write_file.write("\n")
    except IOError:
        print("File not found.")


def get_student_info(**kwargs):
    student_name = kwargs.get("student_name")
    average_score = average_scores(get_test_scores())
    student_info = student_name, "%.2f" % average_score
    write_to_file(student_info)


def average_scores(scores):
    return sum(scores) / len(scores)


def get_test_scores():
    INVALID_INPUT = -2
    STOP = -1
    user_input = 0
    scores = []

    while user_input != STOP:
        try:
            user_input = float(input("Enter a score (enter -1 to exit): "))
        except ValueError:
            user_input = INVALID_INPUT

        if user_input != STOP and user_input != INVALID_INPUT:
            scores.append(user_input)

    return scores


def read_from_file():
    file_dir = os.path.dirname(os.path.abspath(__file__))
    file_name = 'student_info.txt'
    try:
        with open(os.path.join(file_dir, file_name), "r") as read_file:
            for line in read_file:
                print(line.strip())
    except IOError:
        print("File not found.")


if __name__ == '__main__':
    get_student_info(student_name="James Kirk")
    get_student_info(student_name="Wes Brown")
    get_student_info(student_name="Alex Turner")
    get_student_info(student_name="Jimi Hendrix")
    read_from_file()
