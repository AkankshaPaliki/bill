from pizza import Pizza

class DeluxPizza(Pizza):
    def __init__(self, veg):
        super().__init__(veg)

    def add_extra_cheese(self):
        self.price += self.extra_cheese_price

    def add_extra_toppings(self):
        self.price += self.extra_toppings_price

