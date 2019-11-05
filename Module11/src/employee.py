"""
Program: employee.py
Author: Wes Brown
Last date modified: 10/28/19

Purpose: Create the class for employee
"""


class Employee:

    def __init__(self, last_name, first_name, address, phone_number):
        self._last_name = last_name
        self._first_name = first_name
        self._address = address
        self._phone_number = phone_number

    def _format_name(self):
        self._first_name = self._first_name.casefold().capitalize()
        self._last_name = self._last_name.casefold().capitalize()

        return "%s %s" % (self._first_name, self._last_name)

    def display(self):
        print(self._format_name())
        print(self._address)

    def __str__(self) -> str:
        return "First Name: %s; Last Name: %s; Address: %s; Phone Number: %s;" % (
            self._first_name, self._last_name, self._address, self._phone_number)

    def __repr__(self) -> str:
        return self.__str__()
