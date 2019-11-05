"""
Program: salaried_employee.py
Author: Wes Brown
Last date modified: 11/04/19

Purpose: Create the class for salaried employee
"""


import datetime
from Module11.src.employee import Employee


class SalariedEmployee(Employee):
    def __init__(self, last_name, first_name, address, phone_number, start_date, salary):
        super().__init__(last_name, first_name, address, phone_number)
        self._start_date = start_date
        self._salary = salary

    def _get_payment_info(self):
        return "Salaried employee: $%d/year" % self._salary

    def _format_start_date(self):
        return "Start date: %s" % self._start_date.strftime("%x")

    def give_raise(self, raise_amount):
        self._salary = self._salary + raise_amount

    def display(self):
        super().display()
        print(self._format_start_date())
        print(self._get_payment_info())
