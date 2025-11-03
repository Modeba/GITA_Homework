class shopping_cart:
    def __init__(self):
        self.cart = {}
        self.prices = {
            "Bread": 1,
            "Banana": 2,
        }

    def add_item(self, item, quantity):
        self.cart[item] = quantity + self.cart.get(item, 0)
        print(f"Add {quantity} x {item}.")

    def remove_item(self, item, quantity):
        if item not in self.cart:
            print(f"{item} not in cart")
        else:
            self.cart[item] -= quantity
            print(f"REmoved {quantity} x {item}.")

            # Remove negatives
            if self.cart[item] < 0:
                self.cart[item] = 0
    
    def print_current_items(self):
        print(self.cart)

    def calculate_total(self):
        total = 0
        for item in self.cart:
            total += self.cart[item] * self.prices[item]
        print(f"total cost {total}")

cart1 = shopping_cart()

cart1.add_item("Bread", 1)
cart1.print_current_items()
cart1.add_item("Bread", 4)
cart1.print_current_items()

cart1.remove_item("Banana", 3)
cart1.print_current_items()
cart1.remove_item("Bread", 3)
cart1.print_current_items()
cart1.remove_item("Bread", 10)
cart1.print_current_items()

cart1.add_item("Bread", 2)
cart1.print_current_items()
cart1.calculate_total()

cart1.add_item("Banana", 6)
cart1.print_current_items()
cart1.calculate_total()

