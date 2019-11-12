"""
Program: customer_exceptions.py
Author: Wes Brown
Last date modified: 11/11/19

Purpose: Exceptions used in the customer class
"""


class InvalidCustomerIdException(Exception):
    pass


class InvalidNameException(Exception):
    pass


class InvalidPhoneNumberFormat(Exception):
    pass
