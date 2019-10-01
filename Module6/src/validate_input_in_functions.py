"""
Program: validate_input_in_functions.py
Author: Wes Brown
Last date modified: 10/01/19

Purpose: Take score input and validate the score.
"""


"""
Validate the information for a score
:param test_name: mandatory - stores the name of the test
:param test_score: option (default=0) - stores the score of the test (valid range 0-100)
:param invalid_message: optional (default="Invalid test score, try again") - stores the message used for invalid data
"""


def valid_score(score):
    if score > 100 or score < 0:
        return False
    else:
        return True


def score_input(test_name, test_score=0, invalid_message="Invalid test score, try again!"):
    output = invalid_message;

    try:
        if valid_score(test_score):
            output = "%s: %d" % (test_name, test_score)
    except TypeError:
        output = invalid_message  # Don't really need this here, but didn't want a blank catch

    # return {test_name: test_score}
    return output
