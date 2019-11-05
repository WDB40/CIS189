"""
Program: employee_driver.py
Author: Wes Brown
Last date modified: 11/04/19

Purpose: Used to test the hourly and salaried employees
"""
from datetime import datetime

from Module11.src.hourly_employee import HourlyEmployee
from Module11.src.salaried_employee import SalariedEmployee

if __name__ == '__main__':
    today = datetime.today()

    print("Salaried 1: Pre-raise")
    salaried = SalariedEmployee("Brown", "Wes", "111 Main Street", "555-555-5555", today, 40000)
    print(salaried.display())

    print("Salaried 1: Post-raise")
    salaried.give_raise(5000)
    print(salaried.display())

    del salaried

    print("Hourly 2: Pre-raise")
    hourly = HourlyEmployee("Brown", "Wes", "222 2nd Street", "444-444-4444", today, 10)
    print(hourly.display())

    print("Hourly 2: Post-raise")
    hourly.give_raise(2)
    print(hourly.display())

    del hourly


