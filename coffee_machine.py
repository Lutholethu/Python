from pickle import GLOBAL

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

quarter = 0.25
dime = 0.10
nickel = 0.05
penny = 0.01
espresso_cost = 1.50
Latte_cost = 2.50
cappuccino_cost =3.00
amount_inserted = 0

def payment():
    global amount_inserted
    print("Please insert coins to proceed with order")
    quarters = int(input("Enter number of quarters: "))
    dimes = int(input("Enter number of dimes: "))
    nickels = int(input("Enter number of nickels: "))
    pennies = int(input("Enter number of pennies: "))

    amount_inserted = penny * pennies + dime * dimes + nickel * nickels + quarter * quarters

def resource_check():
    espresso_resources = MENU["espresso"]["ingredients"]#to access espresso information
    water_espresso = espresso_resources["water"]
    coffee_espresso = espresso_resources["coffee"]

    latte_resources = MENU["latte"]["ingredients"]
    water_latte = latte_resources["water"]
    milk_latte = latte_resources["milk"]
    coffee_latte = latte_resources["coffee"]

    cappuccino_resources = MENU["cappuccino"]["ingredients"]
    water_cappuccino = cappuccino_resources["water"]
    milk_cappuccino = cappuccino_resources["milk"]
    coffee_cappuccino = cappuccino_resources["coffee"]

    water_resource = resources["water"]
    milk_resource = resources["milk"]
    coffee_resource =resources["coffee"]


    if water_resource < water_espresso or coffee_resource < coffee_espresso:
        print("Machine has insufficient resources to complete the order")
        return False
    elif water_resource < water_latte or coffee_resource < coffee_latte or milk_resource < milk_latte:
        print("Machine has insufficient resources to complete the order")
        return False
    elif water_resource < water_cappuccino or milk_resource < milk_cappuccino or coffee_resource < coffee_cappuccino:
        print("Machine has insufficient resources to complete the order")
        return False


def coffee_order():
    order = input("What would you like to order? (espresso/latte/cappuccino):").lower()
    if order == 'espresso':
        resource_check()
        payment()
        if amount_inserted >= espresso_cost:
            change = round(amount_inserted - espresso_cost, 2)
            print(f"Your change is: ${change}")
        else: #amount_inserted < espresso_cost
            print("You have insufficient funds to complete order.")
            return False

    elif order == 'latte':
        resource_check()
        payment()
        if amount_inserted >= Latte_cost:
            change = round(amount_inserted - Latte_cost, 2)
            print(f"Your change is: {change}")
        else: # amount_inserted < latte_cost
            print("You have insufficient funds to complete order.")
            return False

    elif order == 'cappuccino':
        resource_check()
        payment()
        if amount_inserted >= cappuccino_cost:
            change = round(amount_inserted - cappuccino_cost, 2)
            print(f"Your change is: ${change}")
        else: # amount_inserted < cappuccino_cost
            print("You have insufficient funds to complete order.")
            return False

coffee_order()
