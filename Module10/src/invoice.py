"""
Program: invoice.py
Author: Wes Brown
Last date modified: 10/28/19

Purpose: Create the class for invoice
"""


def _get_tax(value):
    TAX_RATE = 0.06
    return value * TAX_RATE


class Invoice:

    def __init__(self, invoice_id, customer_id, last_name, first_name, phone_number, address, items_with_price=None):
        self.invoice_id = invoice_id
        self.customer_id = customer_id
        self.last_name = last_name
        self.first_name = first_name
        self.phone_number = phone_number
        self.address = address

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
    def customer_id(self):
        return self._customer_id

    @customer_id.setter
    def customer_id(self, value):
        self._customer_id = value

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        self._last_name = value

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        self._first_name = value

    @property
    def phone_number(self):
        return self._phone_number

    @phone_number.setter
    def phone_number(self, value):
        self._phone_number = value

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value

    @property
    def items_with_price(self):
        return self._items_with_price

    @items_with_price.setter
    def items_with_price(self, value):
        self._items_with_price = value

    def __str__(self) -> str:
        return "Invoice ID: %d; Customer ID: %d; Last Name: %s; First Name: %s; Phone Number: %s; Address: %s" % (
        self.invoice_id, self.customer_id, self.last_name, self.first_name, self.phone_number, self.address)

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
