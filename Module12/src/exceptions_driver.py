"""
Program: exceptions_driver.py
Author: Wes Brown
Last date modified: 11/11/19

Purpose: Testing the exceptions again outside of the actual tests...
"""


from Module12.src.customer import Customer
from Module12.src.customer_exceptions import *


if __name__ == '__main__':
    valid_customer_for_printing = Customer("5555", "Brown", "Wes", "555-555-5555")
    print(valid_customer_for_printing)

    try:
        customer = Customer("999", "Brown", "Wes", "555-555-5555")
    except InvalidCustomerIdException:
        print("Caught invalid customer id.")

    try:
        customer = Customer("5555", "123", "Wes", "555-555-5555")
    except InvalidNameException:
        print("Caught invalid last name.")

    try:
        customer = Customer("5555", "Brown", "123", "555-555-5555")
    except InvalidNameException:
        print("Caught invalid first name.")

    try:
        customer = Customer("5555", "Brown", "Wes", "555-5555-5555")
    except InvalidPhoneNumberFormat:
        print("Caught invalid phone number.")
