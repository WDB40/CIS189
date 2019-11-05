"""
Program: manager.py
Author: Wes Brown
Last date modified: 11/04/19

Purpose: Create the class for manager
"""
from Module11.src.multi_inheritence.employee import Employee
from Module11.src.multi_inheritence.person import Person


class Manager(Employee, Person):
    def __init__(self, last_name, first_name, address, phone_number, start_date, salary, department, direct_reports=None):
        Person.__init__(self, last_name, first_name, address, phone_number)
        Employee.__init__(self, start_date, salary)
        self.department = department
        if direct_reports is None:
            direct_reports = list()
        self.direct_reports = direct_reports

    @property
    def department(self):
        return self._department

    @department.setter
    def department(self, value):
        self._department = value

    @property
    def direct_reports(self):
        return self._direct_reports

    @direct_reports.setter
    def direct_reports(self, value):
        self._direct_reports = value

    def give_raise(self, raise_amount):
        self.salary = self.salary + raise_amount

    def display_directs(self):
        directs = "Directs: "
        for employee in self.direct_reports:
            directs = f"{directs}\n{employee}"

        return directs

    def display(self):
        return f"{Person.display(self)}\n{Employee.display(self)}\nDepartment: {self.department}\n{self.display_directs()}"
