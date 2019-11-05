"""
Program: employee.py
Author: Wes Brown
Last date modified: 11/04/19

Purpose: Create the class for employee
"""


import datetime


class Employee:
    def __init__(self, start_date, salary):
        self.start_date = start_date
        self.salary = salary

    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, value):
        self._start_date = value

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        self._salary = value

    def give_raise(self, raise_amount):
        self.salary = self.salary + raise_amount

    def display(self):
        return f"Start Date: {self.start_date.strftime('%x')}; Salary: ${self.salary}"

    def __str__(self) -> str:
        return self.display()

    def __repr__(self) -> str:
        return self.display()
