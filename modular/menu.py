# menu.py - Menu data and menu display

def get_menu():
    return {
        "A1": {"name": "Chicken Burger", "price": 85.00},
        "A2": {"name": "Cheeseburger", "price": 95.00},
        "A3": {"name": "Chicken Meal", "price": 135.00},
        "A4": {"name": "French Fries", "price": 55.00},
        "A5": {"name": "Chicken Nuggets", "price": 75.00},
        "A6": {"name": "Spaghetti", "price": 90.00},
        "A7": {"name": "Soft Drink", "price": 40.00},
        "A8": {"name": "Iced Tea", "price": 45.00},
    }


def display_menu(menu):
    print("\n" + "=" * 55)
    print("                 CECILIA'S FAST FOOD")
    print("                      FULL MENU")
    print("=" * 55)
    print(f"{'Code':<8}{'Menu Item':<30}{'Price':>10}")
    print("-" * 55)

    for code, item in menu.items():
        print(f"{code:<8}{item['name']:<30}₱{item['price']:>8.2f}")

    print("=" * 55)
