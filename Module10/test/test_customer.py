"""
Program: test_customer.py (customer.py)
Author: Wes Brown
Last date modified: 10/28/19

Purpose: Test for the class for customer
"""

from Module10.src.customer import Customer

if __name__ == '__main__':
    customer1 = Customer("123", "Jones", "Mary", "444-444-4444", "222 2nd Street, Des Moines, IA")
    print(customer1.display())

    customer2 = Customer("ABC", "Brown", "Wes", "555-555-5555", "111 Main Street, Des Moines, IA")
    print(customer2.display())

    # Entirely sure what the assignment was asking for, but based on what's there, the exception comes from the constructor
    # Since all the fields are required and the data type for the customer ID is a number, we will raise the error during construction
    # because the constructor uses the setter for the field.
