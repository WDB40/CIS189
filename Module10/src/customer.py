"""
Program: customer.py
Author: Wes Brown
Last date modified: 10/28/19

Purpose: Create the class for customer
"""


class Customer:

    def __init__(self, customer_id, last_name, first_name, phone_number, address):
        self.customer_id = customer_id
        self.last_name = last_name
        self.first_name = first_name
        self.phone_number = phone_number
        self.address = address

    @property
    def customer_id(self):
        return self._customer_id

    @customer_id.setter
    def customer_id(self, value):
        if not value.isdigit():
            raise AttributeError
        else:
            self._customer_id = int(value)

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        self._last_name = value

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        self._first_name = value

    @property
    def phone_number(self):
        return self._phone_number

    @phone_number.setter
    def phone_number(self, value):
        self._phone_number = value

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value

    def __str__(self) -> str:
        return "Customer ID: %d; Last Name: %s; First Name: %s; Phone Number: %s; Address: %s;" % (self.customer_id, self.last_name, self.first_name, self.phone_number, self.address)

    def __repr__(self) -> str:
        return "[Customer]: " + self.__str__()

    def display(self):
        return self.__repr__()
