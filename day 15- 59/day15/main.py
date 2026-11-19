logo = '''

                        ad88    ad88            88                         
                        d8"     d8"             ""                         
                        88      88                                         
 ,adPPYba, ,adPPYYba, MM88MMM MM88MMM ,adPPYba, 88 8b,dPPYba,   ,adPPYba,  
a8"     "" ""     `Y8   88      88   a8P_____88 88 88P'   `"8a a8P_____88  
8b         ,adPPPPP88   88      88   8PP""""""" 88 88       88 8PP"""""""  
"8a,   ,aa 88,    ,88   88      88   "8b,   ,aa 88 88       88 "8b,   ,aa  
 `"Ybbd8"' `"8bbdP"Y8   88      88    `"Ybbd8"' 88 88       88  `"Ybbd8"'

'''
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
    "total sales": 0
}

def check_resource_sufficient(coffee_choice):

    for needed_resources, resources_amount in MENU[coffee_choice]["ingredients"].items():
        if resources_amount > resources[needed_resources]:
            print( f"Sorry! There is not enough {needed_resources}. ")
            return False

    else:
        return True


def can_buy_or_not(inserted_money, coffee_choice):
    coffee_cost =  MENU[coffee_choice]["cost"]

    if inserted_money < coffee_cost:
        print("Not enough money to purchase. Money refunded.")
        return False

    elif inserted_money >= coffee_cost:
        resources["total sales"] += coffee_cost
        return f'Thank you! Here is your change: {round(inserted_money - coffee_cost, 2)}€. '

    else:
        return None


def make_coffee(coffee_choice):

    for needed_resources, resources_amount in MENU[coffee_choice]["ingredients"].items():
        resources[needed_resources] -= resources_amount

    return f"Here is your {coffee_choice}. Enjoy!"


machine_on = True
while machine_on:
    print(logo)
    coffee_option = input("What would you like to have? Type in your option 'espresso'/ 'latte'/ 'cappuccino'.\nOr type 'off' to turn the machine off, or 'report' to check more info. ")

    if coffee_option == "off".strip():
        break

    elif coffee_option == "report".strip():
        for ingredients, amount in resources.items():
            if ingredients == "water" or ingredients == "milk":
                print(f"{ingredients.capitalize()}: {amount}ml.")
            elif ingredients == "coffee":
                print(f"{ingredients.capitalize()}: {amount}g.")
            elif ingredients == "total sales":
                print(f"{ingredients.capitalize()}: {amount}€.")
        exit_report = input("Type 'Enter' to exit report")
        continue


    resource_result = check_resource_sufficient(coffee_option)
    print("\n" * 2)

    if not resource_result == True:
        continue

    print("Please insert coins.")
    insert_quarters = int(input("How many quarters?: 0.25€ "))
    insert_dimes = int(input("How many dimes? 0.1€"))
    insert_nickles = int(input("How many nickles? 0.05€ "))
    insert_pennies = int(input("How many pennies? 0.01€ "))
    print("\n" * 2)
    insert_total = 0.25*insert_quarters + 0.1 *insert_dimes + 0.05*insert_nickles + 0.01*insert_pennies
    print(f"You have deposited {insert_total}€. ")

    buy_result = can_buy_or_not(insert_total, coffee_choice=coffee_option)

    if buy_result == False:
        continue

    print(buy_result)

    coffee_finally = make_coffee(coffee_option)
    print(coffee_finally)
    fill_another_cup = input("Tap 'Enter' to reboot the machine")






