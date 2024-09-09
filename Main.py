from pizza import Pizza, DeluxPizza

def main():
    print("---------------------------------------------Welcome to Pizzamania---------------------------------------------")
    print("Which pizza: (1.Veg Pizza  2.Non Veg Pizza  3.Delux Veg Pizza  4.Delux Non Veg Pizza) ===> ")
    
    ch = int(input())
    
    if ch == 1:
        veg_pizza = Pizza(is_veg=True)
        veg_pizza.add_extra_toppings()
        veg_pizza.add_extra_cheese()
        veg_pizza.take_away()
        veg_pizza.get_bill()
    elif ch == 2:
        nonveg_pizza = Pizza(is_veg=False)
        nonveg_pizza.add_extra_toppings()
        nonveg_pizza.add_extra_cheese()
        nonveg_pizza.take_away()
        nonveg_pizza.get_bill()
    elif ch == 3:
        veg = DeluxPizza(is_veg=True)
        veg.base_pizza_price = 550
        veg.add_extra_toppings()
        veg.add_extra_cheese()
        veg.take_away()
        veg.get_bill()
    elif ch == 4:
        nonveg = DeluxPizza(is_veg=False)
        nonveg.base_pizza_price = 650
        nonveg.add_extra_toppings()
        nonveg.add_extra_cheese()
        nonveg.take_away()
        nonveg.get_bill()
    else:
        print("Sorry Enter again!!!")
        return

if __name__ == "__main__":
    main()

