"""
Program: test_employee.py (employee.py)
Author: Wes Brown
Last date modified: 10/28/19

Purpose: Testing the class for employee
"""

from Module10.src.employee import Employee

if __name__ == '__main__':
    salaried_employee = Employee("John", "Brown", "111 Main Street, Charleston, WV", "555-555-5555", True, "12/12/2012", 80000)
    hourly_employee = Employee("Jane", "Jones", "222 2nd Street, Des Moines, IA", "444-444-4444", False, "11/11/2011", 15.75)

    print("SALARIED")
    salaried_employee.display()
    print("HOURLY")
    hourly_employee.display()

    print("USING __STR___")
    print(salaried_employee)
    print(hourly_employee)

    print("USING __REPRE__")
    print(salaried_employee.__repr__())
    print(hourly_employee.__repr__())
