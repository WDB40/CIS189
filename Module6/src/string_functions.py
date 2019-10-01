"""
Program: string_functions.py
Author: Wes Brown
Last date modified: 10/01/19

Purpose: Functions related to string and manipulating them.
"""

"""
This repeats an entered message a number of times.
:param message: this is the message that will be repeated
:param n: this is the number of times the message will be repeated
:returns multiple_message: the message repeated n number of times
"""


def multiply_string(message, n):
    multiple_message = ""

    for i in range(0, n):
        multiple_message = multiple_message + message

    return multiple_message
