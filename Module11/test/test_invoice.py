"""
Program: test_invoice.py (invoice.py)
Author: Wes Brown
Last date modified: 11/04/19

Purpose: Test the class for invoice with the customer object in it.
"""

from Module11.src.invoice import Invoice, Customer

if __name__ == '__main__':
    my_customer = Customer(555, "Brown", "Wes", "555-555-5555", "111 Main Street, Des Moines, IA")
    my_invoice = Invoice(10, my_customer)
    my_invoice.add_item("Watch", 250.00)
    my_invoice.add_item("Phone", 1000.50)
    my_invoice.add_item("TV", 850.75)
    print(my_invoice)
    my_invoice.create_invoice()

    captain_mal = Customer(1, 'Reynolds', 'Mel', 'No phones', 'Firefly, somewhere in the verse')
    invoice = Invoice(1, captain_mal)
    invoice.add_item('iPad', 799.99)
    invoice.add_item('Surface', 999.99)
    print(invoice)
    invoice.create_invoice()
