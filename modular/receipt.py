# receipt.py - Prints the final receipt


def print_receipt(orders, subtotal, discount, total):
    print("\n")
    print("=" * 60)
    print("                 CECILIA'S FAST FOOD")
    print("                   OFFICIAL RECEIPT")
    print("=" * 60)

    print(f"{'Item':<25}{'Qty':>6}{'Price':>12}{'Total':>13}")
    print("-" * 60)

    for item in orders.values():
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
