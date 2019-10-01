"""
Program: string_functions.py
Author: Wes Brown
Last date modified: 10/01/19

Purpose: Functions related to string and manipulating them.
"""


def multiply_string(message, n):
    multiple_message = ""

    for i in range(0, n):
        multiple_message = multiple_message + message

    return multiple_message
