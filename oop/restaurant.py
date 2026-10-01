# restaurant.py - RestaurantOrderingSystem class (controls the whole flow)
from menu import Menu
from order import Order


class RestaurantOrderingSystem:
    def __init__(self):
        self.menu = Menu()
        self.order = Order()

    def ask_yes_no(self, prompt):
        while True:
            answer = input(prompt).strip().lower()

            if answer in ["yes", "y"]:
                return True
            elif answer in ["no", "n"]:
                return False
            else:
                print("Invalid answer. Please enter yes or no.")

    def get_menu_item(self):
        while True:
            code = input("\nEnter menu code: ").strip().upper()

            if self.menu.has_item(code):
                return code

            print("Invalid menu code. Please choose an item from the menu.")

    def get_quantity(self):
        while True:
            try:
                quantity = int(input("Enter quantity: "))

                if quantity > 0:
                    return quantity

                print("Quantity must be greater than zero.")

            except ValueError:
                print("Invalid quantity. Please enter a whole number.")

    def run(self):
        print("\n" + "=" * 55)
        print("          WELCOME TO CECILIA'S FAST FOOD")
        print("=" * 55)

        self.menu.display()

        if not self.ask_yes_no("\nWould you like to order? (yes/no): "):
            print("\nThank you for visiting Cecilia's Fast Food!")
            print("Have a great day!")
            return

        while True:
            code = self.get_menu_item()
            quantity = self.get_quantity()

            self.order.add_item(code, self.menu.get_item(code), quantity)
            print("\nItem successfully added to your order!")

            if not self.ask_yes_no("\nWould you like to order another item? (yes/no): "):
                break

        self.order.print_receipt()
