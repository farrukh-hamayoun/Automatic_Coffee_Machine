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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_resourse_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print("“Sorry there is not enough water.")
            return False
    return True


def process_coins():
    print("Please Insert Your Coins")
    total =int(input("How many Quarters\t"))* 0.25
    total +=int(input("How many Dimes\t"))* 0.10
    total +=int(input("How many nickles\t"))*0.05
    total +int(input("How many pennies\t"))*0.01
    return total


def is_transiotion_successful(money_received, drink_cost):
    if money_received >= drink_cost:
        global profit
        change = round(money_received - drink_cost)
        print(f"here is your change ${change}")
        profit += money_received
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(user_choise, ordered_ingredients):
    for item in ordered_ingredients:
        resources[item] -= ordered_ingredients[item]
    print(f"Here is your Coffee, {user_choise}")


check = True
while check:
    choice = input("What would you like? (espresso/latte/cappuccino):").lower()
    if choice == "off":
        check = False
    elif choice == "report":
        print(f"Water: {resources['water']}")
        print(f"Milk: {resources['milk']}")
        print(f"Coffee: {resources['coffee']}")
        print(f"Profit: ${profit}")
    else:
        drink = MENU[choice]
        if is_resourse_sufficient(drink["ingredients"]):
            if is_transiotion_successful(process_coins(), drink["cost"]):
                make_coffee(choice, drink["ingredients"])