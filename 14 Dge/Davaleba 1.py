class shopping_cart:
    def __init__(self):
        self.cart = {}
    
    def add_item(self, item, quantity):
        self.cart[item] = quantity + self.cart.get(item, 0)
        print(f"დაემატა {quantity} x {item}.")

    def remove_item(self, item, quantity):
        if item not in self.cart:
            print(f'{item} არ არის კალათაში')
        else:
            self.cart[item] -= quantity
            print(f"მოშორდა {quantity} x {item}.")

            # Remove negatives
            if self.cart[item] < 0:
                self.cart[item] = 0

cart1 = shopping_cart()

cart1.add_item("პური", 1)
print(cart1.cart)
cart1.add_item("პური", 4)
print(cart1.cart)

cart1.remove_item("ბანანი", 3)
print(cart1.cart)
cart1.remove_item("პური", 3)
print(cart1.cart)
cart1.remove_item("პური", 10)
print(cart1.cart)

cart1.add_item("პური", 2)
print(cart1.cart)