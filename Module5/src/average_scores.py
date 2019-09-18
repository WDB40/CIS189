"""
Program: average_scores.py
Author: Wes Brown
Last date modified: 09/17/19

Purpose: Calculate the average from the list of values instead of passing each
"""


def average(score_list):
    total = 0
    num_values = len(score_list)
    avg_score = -1

    if num_values != 0:
        for value in score_list:
            total = total + value
        avg_score = total / len(score_list)
    else:
        avg_score = 0

    return avg_score


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


if __name__ == '__main__':
    last_name = input("Enter the last name: ")
    first_name = input("Enter the first name: ")
    avg_scores = average(get_test_scores())

    print("%s, %s - %.2f" % (last_name, first_name, avg_scores))
