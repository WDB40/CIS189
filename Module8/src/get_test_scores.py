"""
Program: get_test_scores.py
Author: Wes Brown
Last date modified: 10/15/19

Purpose:
"""


def valid_number(value, min, max):
    INVALID_INPUT = -1

    if value < min or value > max or value == INVALID_INPUT:
        return False
    else:
        return True


def get_test_score():
    INVALID_INPUT = -1
    MAX_SCORE = 100
    MIN_SCORE = 0
    user_input = INVALID_INPUT

    while not valid_number(user_input, MIN_SCORE, MAX_SCORE):
        try:
            user_input = int(input("Enter a test score: "))
        except ValueError:
            user_input = INVALID_INPUT

    return user_input


def average_scores(the_dict):
    total = 0

    for key in the_dict:
        total = total + the_dict[key]

    return total / len(the_dict)


if __name__ == '__main__':
    num_scores = int(input("Enter the number of test scores: "))
    scores_dict = dict()

    for i in range(1, num_scores + 1):
        score = get_test_score()
        scores_dict.update({i: score})

    print("Average Score: %.2f" % average_scores(scores_dict))
