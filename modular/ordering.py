# ordering.py - Everything that asks the customer for input


def ask_to_order():
    while True:
        answer = input("\nWould you like to order? (yes/no): ").strip().lower()

        if answer in ["yes", "y"]:
            return True
        elif answer in ["no", "n"]:
            return False
        else:
            print("Invalid answer. Please enter yes or no.")


def get_menu_item(menu):
    while True:
        item_code = input("\nEnter menu code: ").strip().upper()

        if item_code in menu:
            return item_code

        print("Invalid menu code. Please choose an item from the menu.")


def get_quantity():
    while True:
        try:
            quantity = int(input("Enter quantity: "))

            if quantity > 0:
                return quantity

            print("Quantity must be greater than zero.")

        except ValueError:
            print("Invalid quantity. Please enter a whole number.")


def add_order(orders, menu, item_code, quantity):
    if item_code in orders:
        orders[item_code]["quantity"] += quantity
    else:
        orders[item_code] = {
            "name": menu[item_code]["name"],
            "price": menu[item_code]["price"],
            "quantity": quantity,
        }


def ask_another_order():
    while True:
        answer = input("\nWould you like to order another item? (yes/no): ").strip().lower()

        if answer in ["yes", "y"]:
            return True
        elif answer in ["no", "n"]:
            return False
        else:
            print("Invalid answer. Please enter yes or no.")
