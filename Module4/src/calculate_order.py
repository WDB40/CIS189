"""
Program: calculate_order.py
Author: Wes Brown
Last date modified: 09/16/19

Purpose: To calculate an order with discounts, shipping, and tax.
"""

def calculate_tax(amount):
    tax_amount = 0.06
    return amount * tax_amount


def calculate_shipping(amount):

    if amount < 0:
        shipping_cost = -1
    elif amount < 10:
        shipping_cost = 5.95
    elif amount < 30:
        shipping_cost = 7.95
    elif amount < 50:
        shipping_cost = 11.95
    else:
        shipping_cost = 0

    return shipping_cost


def add_discounts(price, cash_coupon, percent_coupon):
    # Honest answer, I'd just use the below, but from the rubric, we need a nested if, so I did it with that.
    # return (price - cash_coupon) * (1 - percent_coupon)

    discount_price = price

    if cash_coupon > 0:
        discount_price = discount_price - cash_coupon
        if percent_coupon > 0:
            discount_price = discount_price * (1 - percent_coupon)
    elif percent_coupon > 0:
        discount_price = discount_price * (1 - percent_coupon)

    return discount_price


def calculate_order(price, cash_coupon, percent_coupon):
    discount_price = add_discounts(price, cash_coupon, percent_coupon)
    total = discount_price + calculate_tax(discount_price) + calculate_shipping(discount_price)

    return total
