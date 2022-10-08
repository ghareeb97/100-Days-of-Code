MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
piggy_bank = 0
resources = {
    "water": 500,
    "milk": 200,
    "coffee": 100,
}


def calculate_change(coffee, quarter, dime, nickle, penny):
    bill = MENU[coffee]["cost"]
    total_paid = (quarter * 25 + dime * 10 + nickle * 5 + penny) / 100
    return round(total_paid - bill, 2)


def enough_money(coffee, quarter, dime, nickle, penny):
    bill = MENU[coffee]["cost"]
    total_paid = (quarter * 25 + dime * 10 + nickle * 5 + penny) / 100
    if total_paid < bill:
        return False
    else:
        return True


def remaining_resources(coffee):
    """
Deduct the used resources.
    :param coffee: key
    """
    if resources["water"] >= MENU[coffee]["ingredients"]["water"] and resources["milk"] >= MENU[coffee]["ingredients"]["milk"] and resources["coffee"] >= MENU[coffee]["ingredients"]["coffee"]:
        resources["water"] -= MENU[coffee]["ingredients"]["water"]
        resources["milk"] -= MENU[coffee]["ingredients"]["milk"]
        resources["coffee"] -= MENU[coffee]["ingredients"]["coffee"]


def not_enough(coffee):
    """
Check if there is enough resources to make the coffee
    :param coffee: key
    :return: Print the missing ingredient and boolean
    """
    for item in resources:
        if resources[item] < MENU[coffee]["ingredients"][item]:
            print(f"There is no {item} remaining")
            return True

    return False


def coffee_machine(profit):
    is_on = True
    while is_on:
        coffee_requested = input(" What would you like? (espresso/latte/cappuccino): ")
        if coffee_requested == "report":
            print(f"Water: {resources['water']}ml")
            print(f"Milk: {resources['milk']}ml")
            print(f"Coffee: {resources['coffee']}g")
            print(f"Money: ${profit}")
        elif coffee_requested == "off":
            is_on = False
        elif not_enough(coffee_requested):
            coffee_machine(profit)
        else:
            print("Please insert coins.")
            quarters = int(input("how many quarters?: "))
            dimes = int(input("how many dimes?: "))
            nickles = int(input("how many nickles?: "))
            pennies = int(input("how many pennies?: "))
            if enough_money(coffee_requested, quarters, dimes, nickles, pennies):
                change = calculate_change(coffee_requested, quarters, dimes, nickles, pennies)
                profit += MENU[coffee_requested]["cost"]
                print(f"Here are ${change}.")
                print(f"Here is your {coffee_requested} ☕️. Enjoy!")
                remaining_resources(coffee_requested)
            else:
                print("Sorry that's not enough money. Money refunded.")
                coffee_machine(profit)


coffee_machine(piggy_bank)
