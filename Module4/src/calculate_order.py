def calculate_tax(amount):
    pass


def calculate_shipping(amount):
    shipping_cost = -1
    amount = int(amount)

    if amount < 10:
        shipping_cost = 5.95
    elif amount < 30:
        shipping_cost = 7.95
    elif amount < 50:
        shipping_cost = 11.95
    elif shipping_cost >= 50:
        shipping_cost = 0

    return shipping_cost


def add_discounts(cash_coupon, percent_coupon):
    pass


def calculate_order(price, cash_coupon, percent_coupon):
    pass
