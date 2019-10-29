"""
Program: employee.py
Author: Wes Brown
Last date modified: 10/28/19

Purpose: Create the class for employee
"""

import datetime


def _create_date(start_date):
    date_values = str(start_date).split("/")
    return datetime.datetime(int(date_values[2]), int(date_values[1]), int(date_values[0]))


class Employee:

    def __init__(self, last_name, first_name, address, phone_number, salaried, start_date, salary):
        self._last_name = last_name
        self._first_name = first_name
        self._address = address
        self._phone_number = phone_number
        self._salaried = salaried
        self._start_date = _create_date(start_date)
        self._salary = salary

    def _get_payment_info(self):
        if self._salaried:
            payment_info = "Salaried employee: $%d/year" % self._salary
        else:
            payment_info = "Hourly employee: $%.2f/hour" % self._salary

        return payment_info

    def _format_name(self):
        self._first_name = self._first_name.casefold().capitalize()
        self._last_name = self._last_name.casefold().capitalize()

        return "%s %s" % (self._first_name, self._last_name)

    def _format_start_date(self):
        return "Start date: %s" % self._start_date

    def display(self):
        print(self._format_name())
        print(self._address)
        print(self._get_payment_info())
        print(self._format_start_date())

    def __str__(self) -> str:
        return "First Name: %s; Last Name: %s; Address: %s; Phone Number: %s; Salaried: %r; Start Date: %s; Pay: %.2f" % (
            self._first_name, self._last_name, self._address, self._phone_number, self._salaried, self._start_date,
            self._salary)

    def __repr__(self) -> str:
        return self.__str__()
