"""
Program: average_scores.py
Author: Wes Brown
Last date modified: 10/07/19

Purpose: Using tuples in Python
"""


def average_scores(*args, **kwargs):
    average = sum(args)/len(args)
    first_name = kwargs.get("first_name")
    last_name = kwargs.get("last_name")
    course = kwargs.get("course")
    return "Name: %s, %s - Course: %s - GPA: %.2f" % (last_name, first_name, course, average)


if __name__ == '__main__':
    print(average_scores(88, 89, 90, 91, 92, first_name="Wes", last_name="Brown", course="Java 2"))
    print(average_scores(0, 20, 40, 60, 80, 100, first_name="John", last_name="Wayne", course="Early American History"))
    print(average_scores(90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, first_name="Daniel", last_name="Craig", course="Espionage"))
