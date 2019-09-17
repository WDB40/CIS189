"""
Program: basic_for_loop.py
Author: Wes Brown
Last date modified: 09/17/19

Purpose: To begin using for loops in python
"""


def print_list(input_list):
    for item in input_list:
        print(item)


def print_descending_odd_numbers(start, finish):
    for i in range(start, finish-1, -1):
        if i % 2 == 1:
            print(i)


if __name__ == '__main__':
    floating_nums = [1.1, 2.2, 3.3, 4.4, 5.5]
    print_list(floating_nums)
    print_descending_odd_numbers(99, 33)
