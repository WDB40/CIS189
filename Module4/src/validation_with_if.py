"""
Program: validations_with_if.py
Author: Wes Brown
Last date modified: 09/16/19

Purpose: To average 3 scores.
"""


def average(score1, score2, score3):
    NUMBER_TESTS = 3

    if score1 < 0 or score2 < 0 or score3 < 0:
        average_score = -1
    else:
        average_score = float((score1 + score2 + score3) / NUMBER_TESTS)

    return average_score
