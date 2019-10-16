"""
Program: half_birthday.py
Author: Wes Brown
Last date modified: 10/15/19

Purpose: Use datetime to calculate a half-birthday
"""


from datetime import timedelta, date, datetime
from dateutil.relativedelta import *


def half_birthday(birthday):
    return birthday + relativedelta(months=6)


if __name__ == '__main__':
    pass
