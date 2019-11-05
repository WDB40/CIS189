"""
Program: person.py
Author: Wes Brown
Last date modified: 11/04/19

Purpose: Create the class for person
"""


class Person:
    def __init__(self, last_name, first_name, address, phone_number):
        self.last_name = last_name
        self.first_name = first_name
        self.address = address
        self.phone_number = phone_number

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
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value

    @property
    def phone_number(self):
        return self._phone_number

    @phone_number.setter
    def phone_number(self, value):
        self._phone_number = value

    def display(self):
        return f"Last Name: {self.last_name}; First Name{self.first_name}; Address: {self.address}; Phone Number: {self.phone_number}"

    def __str__(self) -> str:
        return self.display()

    def __repr__(self) -> str:
        return self.display()
