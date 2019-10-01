"""
Program: multiply_string.py
Author: Wes Brown
Last date modified: 10/01/19

Purpose: Takes a message and number then prints the message that number of times.
"""


def multiply_string(message, n):
    multiple_message = ""

    for i in range(0, n):
        multiple_message = multiple_message + message + " "

    return multiple_message


if __name__ == '__main__':
    print(multiply_string("Java", 2))
    print(multiply_string("Java", 3))
    print(multiply_string("Java", 4))
    print(multiply_string("Java", 5))
    print(multiply_string("Java", 6))
    print(multiply_string("Java", 7))
