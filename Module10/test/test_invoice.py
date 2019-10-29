"""
Program: test_invoice.py (invoice.py)
Author: Wes Brown
Last date modified: 10/28/19

Purpose: Test the class for invoice
"""

from Module10.src.invoice import Invoice

if __name__ == '__main__':
    my_invoice = Invoice(10, 555, "Brown", "Wes", "555-555-5555", "111 Main Street, Des Moines, IA")
    my_invoice.add_item("Watch", 250.00)
    my_invoice.add_item("Phone", 1000.50)
    my_invoice.add_item("TV", 850.75)
    my_invoice.create_invoice()
