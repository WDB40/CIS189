"""
Program: validations_with_try.py
Author: Wes Brown
Last date modified: 09/16/19

Purpose: To average 3 scores with exceptions.
"""


def average(score1, score2, score3):
    NUMBER_TESTS = 3

    if score1 < 0 or score2 < 0 or score3 < 0:
        raise ValueError
    else:
        average_score = float((score1 + score2 + score3) / NUMBER_TESTS)

    return average_score


if __name__ == '__main__':

    try:
        print(average(-1, 90, 90))
    except ValueError:
        print("An error occurred")
    else:
        print("Nothing bad happened")
    finally:
        print("We tried, at least. Not sure how it went.")
