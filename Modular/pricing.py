# pricing.py - Subtotal and discount computations


def calculate_subtotal(orders):
    subtotal = 0

    for item in orders.values():
        subtotal += item["price"] * item["quantity"]

    return subtotal


def calculate_discount(subtotal):
    # 5% off if the subtotal reaches P500
    if subtotal >= 500:
        return subtotal * 0.05

    return 0
