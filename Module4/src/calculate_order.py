def calculate_tax(amount):
    tax_amount = 0.06;
    amount = float(amount)
    return amount * tax_amount


def calculate_shipping(amount):
    amount = float(amount)

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


def add_discounts(cash_coupon, percent_coupon):
    pass


def calculate_order(price, cash_coupon, percent_coupon):
    pass
