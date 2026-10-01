# main.py - Modular version: imports and runs everything
from menu import get_menu, display_menu
from ordering import (
    ask_to_order,
    get_menu_item,
    get_quantity,
    add_order,
    ask_another_order,
)
from pricing import calculate_subtotal, calculate_discount
from receipt import print_receipt


def main():
    menu = get_menu()
    orders = {}

    print("\n" + "=" * 55)
    print("          WELCOME TO CECILIA'S FAST FOOD")
    print("=" * 55)

    display_menu(menu)

    if not ask_to_order():
        print("\nThank you for visiting Cecilia's Fast Food!")
        print("Have a great day!")
        return

    while True:
        item_code = get_menu_item(menu)
        quantity = get_quantity()

        add_order(orders, menu, item_code, quantity)
        print("\nItem successfully added to your order!")

        if not ask_another_order():
            break

    subtotal = calculate_subtotal(orders)
    discount = calculate_discount(subtotal)
    total = subtotal - discount

    print_receipt(orders, subtotal, discount, total)


if __name__ == "__main__":
    main()
