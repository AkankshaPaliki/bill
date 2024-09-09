import sys

class Pizza:
    def __init__(self, veg):
        self.price = 0
        self.veg = veg
        
        self.extra_cheese_price = 100
        self.extra_toppings_price = 150
        self.back_pack_price = 20
        
        self.base_pizza_price = 0
        
        self.is_extra_cheese_added = False
        self.is_extra_toppings_added = False
        self.is_opted_for_takeaway = False
        
        if self.veg:
            self.price = 300
        else:
            self.price = 400
        
        self.base_pizza_price = self.price
    
    def add_extra_cheese(self):
        print("Extra cheese (y/n)?")
        ch = input().lower()
        if ch == 'y':
            self.is_extra_cheese_added = True
            self.price += self.extra_cheese_price
        elif ch == 'n':
            self.is_extra_cheese_added = False
    
    def add_extra_toppings(self):
        print("Want Extra Toppings (y/n)? =>")
        ch = input().lower()
        if ch == 'y':
            self.is_extra_toppings_added = True
            self.price += self.extra_toppings_price
        elif ch == 'n':
            self.is_extra_toppings_added = False
    
    def take_away(self):
        print("Want Takeaway (y/n)? =>")
        ch = input().lower()
        if ch == 'y':
            self.is_opted_for_takeaway = True
            self.price += self.back_pack_price
        elif ch == 'n':
            self.is_opted_for_takeaway = False
    
    def get_bill(self):
        bill = ""
        print(f"Pizza : {self.base_pizza_price}")
        if self.is_extra_cheese_added:
            bill += f"Extra Cheese : {self.extra_cheese_price}\n"
        if self.is_extra_toppings_added:
            bill += f"Extra Toppings : {self.extra_toppings_price}\n"
        if self.is_opted_for_takeaway:
            bill += f"Take way : {self.back_pack_price}\n"
        bill += f"\nTotal Amount : {self.price}\n"
        
        print(bill)
        print("\n\n\nThank you!!! Visit Again.....")
        print("------------------------------------------")

# Example usage:
if __name__ == "__main__":
    veg_pizza = Pizza(True)
    veg_pizza.add_extra_cheese()
    veg_pizza.add_extra_toppings()
    veg_pizza.take_away()
    veg_pizza.get_bill()

