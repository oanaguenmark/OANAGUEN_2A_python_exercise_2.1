# order.py - Order class (the customer's order)


class Order:
    DISCOUNT_THRESHOLD = 500
    DISCOUNT_RATE = 0.05

    def __init__(self):
        self.items = {}

    def add_item(self, code, item, quantity):
        if code in self.items:
            self.items[code]["quantity"] += quantity
        else:
            self.items[code] = {
                "name": item["name"],
                "price": item["price"],
                "quantity": quantity,
            }

    def calculate_subtotal(self):
        subtotal = 0

        for item in self.items.values():
            subtotal += item["price"] * item["quantity"]

        return subtotal

    def calculate_discount(self):
        subtotal = self.calculate_subtotal()

        if subtotal >= self.DISCOUNT_THRESHOLD:
            return subtotal * self.DISCOUNT_RATE

        return 0

    def calculate_total(self):
        return self.calculate_subtotal() - self.calculate_discount()

    def print_receipt(self):
        subtotal = self.calculate_subtotal()
        discount = self.calculate_discount()
        total = self.calculate_total()

        print("\n")
        print("=" * 60)
        print("                 CECILIA'S FAST FOOD")
        print("                   OFFICIAL RECEIPT")
        print("=" * 60)

        print(f"{'Item':<25}{'Qty':>6}{'Price':>12}{'Total':>13}")
        print("-" * 60)

        for item in self.items.values():
            item_total = item["price"] * item["quantity"]

            print(
                f"{item['name']:<25}"
                f"{item['quantity']:>6}"
                f"₱{item['price']:>10.2f}"
                f"₱{item_total:>11.2f}"
            )

        print("-" * 60)
        print(f"{'Subtotal':<43}₱{subtotal:>11.2f}")
        print(f"{'Discount':<43}₱{discount:>11.2f}")
        print(f"{'TOTAL':<43}₱{total:>11.2f}")
        print("=" * 60)
        print("              THANK YOU FOR ORDERING!")
        print("                 PLEASE COME AGAIN!")
        print("=" * 60)
