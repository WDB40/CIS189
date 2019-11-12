"""
Program: test_customer_exceptions.py
Author: Wes Brown
Last date modified: 11/11/19

Purpose: Testing exceptions used in the customer class
"""


import unittest
from Module12.src.customer import Customer
from Module12.src.customer_exceptions import *


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("5555", "Brown", "Wes", "555-555-5555")

    def tearDown(self):
        del self.customer

    def test_invalid_customer_id_low(self):
        with self.assertRaises(InvalidCustomerIdException):
            self.customer.customer_id = "999"

    def test_invalid_customer_id_high(self):
        with self.assertRaises(InvalidCustomerIdException):
            self.customer.customer_id = "10000"

    def test_invalid_last_name(self):
        with self.assertRaises(InvalidNameException):
            self.customer.last_name = "123"

    def test_invalid_first_name(self):
        with self.assertRaises(InvalidNameException):
            self.customer.first_name = "123"

    def test_invalid_phone_format(self):
        with self.assertRaises(InvalidPhoneNumberFormat):
            self.customer.phone_number = "5555555555"

    def test_invalid_phone_format_length(self):
        with self.assertRaises(InvalidPhoneNumberFormat):
            self.customer.phone_number = "555-5555-555"

    def test_invalid_phone_format_numeric(self):
        with self.assertRaises(InvalidPhoneNumberFormat):
            self.customer.phone_number = "a55-a55-a555"

    def test_str_question_mark(self):
        self.assertEqual(self.customer.__str__(), "Customer ID: 5555; Last Name: Brown; First Name: Wes; Phone Number: 555-555-5555;")

    def test_display_question_mark(self):
        self.assertEqual(self.customer.display(), "[Customer]: Customer ID: 5555; Last Name: Brown; First Name: Wes; Phone Number: 555-555-5555;")


if __name__ == '__main__':
    unittest.main()
