"""
Program: customer.py
Author: Wes Brown
Last date modified: 11/11/19

Purpose: Create the class for customer
"""

from Module12.src.customer_exceptions import *


def is_phone_number(value):
    valid_phone = True
    values = str(value).split("-")
    if len(values) != 3:
        valid_phone = False
    else:
        if not values[0].isnumeric() or len(values[0]) != 3:
            valid_phone = False
        if not values[1].isnumeric() or len(values[1]) != 3:
            valid_phone = False
        if not values[2].isnumeric() or len(values[2]) != 4:
            valid_phone = False

    return valid_phone


class Customer:

    def __init__(self, customer_id, last_name, first_name, phone_number):
        self.customer_id = customer_id
        self.last_name = last_name
        self.first_name = first_name
        self.phone_number = phone_number

    @property
    def customer_id(self):
        return self._customer_id

    @customer_id.setter
    def customer_id(self, value):
        if not value.isdigit():
            raise InvalidCustomerIdException
        elif int(value) < 1000 or int(value) > 9999:
            raise InvalidCustomerIdException
        else:
            self._customer_id = int(value)

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        if str(value).isalpha():
            self._last_name = value
        else:
            raise InvalidNameException

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        if str(value).isalpha():
            self._first_name = value
        else:
            raise InvalidNameException

    @property
    def phone_number(self):
        return self._phone_number

    @phone_number.setter
    def phone_number(self, value):
        if is_phone_number(value):
            self._phone_number = value
        else:
            raise InvalidPhoneNumberFormat

    def __str__(self) -> str:
        return "Customer ID: %d; Last Name: %s; First Name: %s; Phone Number: %s;" % (self.customer_id, self.last_name, self.first_name, self.phone_number)

    def __repr__(self) -> str:
        return "[Customer]: " + self.__str__()

    def display(self):
        return self.__repr__()
