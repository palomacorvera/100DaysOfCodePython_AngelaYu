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

profit = 0

def inserted_coins(quarters, dimes, nickles, pennies):
    total_inserted = (pennies * 0.01) + (nickles * 0.05) + (dimes * 0.1) + (quarters * 0.25)
    return total_inserted

choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

choice_info = MENU[choice]
price = choice_info["cost"]
ingredients = choice_info["ingredients"]

print("Please insert coins.")
quarters = int(input("How many quarters?: "))
dimes = int(input("How many dimes?: "))
nickles = int(input("How many nickles?: "))
pennies = int(input("How many pennies?: "))

total_inserted = inserted_coins(quarters, dimes, nickles, pennies)

if price > total_inserted:
   print("Sorry that's not enough money. Money refunded.") 
else:
    if resources["water"] < ingredients["water"] or resources["coffee"] < ingredients["coffee"] or (choice != "espresso" and resources["milk"] < ingredients["milk"]):
        print("Sorry there's not enough resources. Money refunded.") 
    else: 
        profit += price
        resources["water"] -= ingredients["water"]
        resources["coffee"] -= ingredients["coffee"]

        if choice != 'espresso':
            resources["milk"] -= ingredients["milk"]

        if total_inserted > price:
            refound = total_inserted - price
            print(f"Here is ${refound} in change")
        
        print(f"Here is your {choice} ☕️. Enjoy!")