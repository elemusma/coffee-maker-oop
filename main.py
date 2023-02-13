from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


menu = Menu()
get_items = menu.get_items()
# find_drink = menu.find_drink()

# print(MenuItem.cost)

latte = MenuItem(name="latte", water=200, milk=150, coffee=24, cost=2.5)
espresso = MenuItem(name="espresso", water=50, milk=0, coffee=18, cost=1.5)
cappuccino = MenuItem(name="cappuccino", water=250, milk=50, coffee=24, cost=3)




# print(getattr(menu_item,'latte'))

coffee_maker = CoffeeMaker()
# print(get_items)
# print(find_drink)

money_machine = MoneyMachine()

def user_order():

    is_on = True

    while is_on:
        order = input(f"What would you like? ({get_items}): ").lower()
        # cost = 2.5

        # print(cost)
        if order == 'off':
            print("Coffee machine is off. Have a good day!")
            return
        elif order == 'report':
            coffee_maker.report()
            money_machine.report()
        else:
            # print(f"User chose {order}.")
            drink = menu.find_drink(order)
            if coffee_maker.is_resource_sufficient(drink):
                # money_machine.process_coins()
                payment_successful = money_machine.make_payment(drink.cost)
                if payment_successful:
                    coffee_maker.make_coffee(drink)
                    # coffee_maker.report()
                    # money_machine.report()


user_order()

# print("report below")
# money_machine.report()

# print("process_coins below")
# process_coins = money_machine.process_coins()
# print(money_machine.process_coins())

# print("make_payment make payment")
# money_machine.make_payment(10)



# print(Menu)
# print(MenuItem)
# print(CoffeeMaker)
# print(MoneyMachine)