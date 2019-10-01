"""
Program: inner_functions_assignment.py
Author: Wes Brown
Last date modified: 10/01/19

Purpose: Working with inner functions.
"""


def area(rec_measurements):
    if len(rec_measurements) == 2:
        return rec_measurements[0] * rec_measurements[1]


def perimeter(rec_measurements):
    sides_total = 0

    for side in rec_measurements:
        sides_total = sides_total + side

    if len(rec_measurements) == 2:
        return sides_total * 2


def measurements(rec_measurements):
    rec_area = area(rec_measurements)
    rec_perimeter = perimeter(rec_measurements)
    return "Perimeter = %.2f Area = %.2f" % (rec_perimeter, rec_area)
