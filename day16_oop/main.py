from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

is_on = True
while is_on:
    option = menu.get_items()
    choice = input(f"What would you like? ({option}):")

    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if drink is None:
            continue

        has_resource = coffee_maker.is_resource_sufficient(drink)
        if not has_resource:
            continue

        is_payment_success = money_machine.make_payment(drink.cost)
        if not is_payment_success:
            continue

        coffee_maker.make_coffee(drink)
