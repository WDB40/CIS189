"""
Program: hourly_employee_input.py
Author: Wes Brown
Last date modified: 10/01/19

Purpose: Display employee information such as name and pay.
"""


def valid_number(value, min, max):
    INVALID_INPUT = -1

    if value < min or value > max or value == INVALID_INPUT:
        return False
    else:
        return True


def get_name():
    return input("Enter the employee's name: ")


def get_hours_worked():
    INVALID_INPUT = -1
    MIN_HOURS = 15
    MAX_HOURS = 80  # Assuming weekly
    user_input = INVALID_INPUT

    while not valid_number(user_input, MIN_HOURS, MAX_HOURS):
        try:
            user_input = int(input("How many hours did the employee work? "))
        except ValueError:
            user_input = INVALID_INPUT

    return user_input


def get_pay_rate():
    INVALID_INPUT = -1
    MIN_PAY_RATE = 7.25
    MAX_PAY_RATE = 100
    user_input = INVALID_INPUT

    while not valid_number(user_input, MIN_PAY_RATE, MAX_PAY_RATE):
        try:
            user_input = float(input("What is the employee's pay rate? "))
        except ValueError:
            user_input = INVALID_INPUT

    return user_input


def hourly_employee_input():
    emp_name = get_name()
    emp_hours_worked = get_hours_worked()
    emp_pay_rate = get_pay_rate()

    print("Name: %s; Pay Rate: %.2f; Hours Worked: %d" % (emp_name, emp_pay_rate, emp_hours_worked))


if __name__ == '__main__':
    hourly_employee_input()
