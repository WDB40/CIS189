"""
Program: invoice.py
Author: Wes Brown
Last date modified: 11/04/19

Purpose: Create the class for invoice that uses the Customer class
"""

from Module11.src.customer import Customer


def _get_tax(value):
    TAX_RATE = 0.06
    return value * TAX_RATE


class Invoice:

    def __init__(self, invoice_id, customer, items_with_price=None):
        self.invoice_id = invoice_id
        self.customer = customer
        if items_with_price is None:
            items_with_price = dict()
        self.items_with_price = items_with_price

    @property
    def invoice_id(self):
        return self._invoice_id

    @invoice_id.setter
    def invoice_id(self, value):
        self._invoice_id = value

    @property
    def customer(self):
        return self._customer

    @customer.setter
    def customer(self, value):
        self._customer = value

    @property
    def items_with_price(self):
        return self._items_with_price

    @items_with_price.setter
    def items_with_price(self, value):
        self._items_with_price = value

    def display(self):
        print(self.__str__())
        self.create_invoice()

    def __str__(self) -> str:
        return "Invoice ID: %d; Customer ID: %d; Last Name: %s; First Name: %s; Phone Number: %s; Address: %s" % (
            self.invoice_id, self.customer.customer_id, self.customer.last_name, self.customer.first_name,
            self.customer.phone_number, self.customer.address)

    def __repr__(self) -> str:
        return "[Invoice]: " + self.__str__()

    def add_item(self, key, value):
        self._items_with_price[key] = value

    def create_invoice(self):
        items_total = 0

        for key, value in self.items_with_price.items():
            print("%s.....$%.2f" % (key, value))
            items_total = items_total + value

        tax_amount = _get_tax(items_total)
        total = tax_amount + items_total

        print("Tax.....$%.2f" % tax_amount)
        print("Total.....$%.2f" % total)
