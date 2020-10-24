# Write your code here

# global variables

water_storage = 400
milk_storage = 540
coffee_storage = 120
cups_storage = 9
money_storage = 550

program_is_running = True


def show_left_ingredients():
    print("")
    print("The coffee machine has: ")
    print(water_storage, "of water")
    print(milk_storage, "of milk")
    print(coffee_storage, "of coffee beans")
    print(cups_storage, "of disposable cups")
    print("$" + str(money_storage) + " of money")


def calculate_usage_espresso():
    global water_storage
    global coffee_storage
    global money_storage
    global cups_storage
    water_usage = 250
    coffee_usage = 16
    cost = 4
    cups_usage = 1
    if water_storage < water_usage:
        print("Sorry, not enough water!")
    elif coffee_storage < coffee_usage:
        print("Sorry, not enough coffee!")
    elif cups_storage < cups_usage:
        print("Sorry, not enough cups!")
    else:
        print("I have enough resources, making you a coffee!")
        water_storage = water_storage - water_usage
        coffee_storage = coffee_storage - coffee_usage
        money_storage = money_storage + cost
        cups_storage = cups_storage - cups_usage


def output_espresso():
    calculate_usage_espresso()


def calculate_usage_latte():
    global water_storage
    global coffee_storage
    global milk_storage
    global cups_storage
    global money_storage
    water_usage = 350
    milk_usage = 75
    coffee_usage = 20
    cost = 7
    cups_usage = 1
    if water_storage < water_usage:
        print("Sorry, not enough water!")
    elif coffee_storage < coffee_usage:
        print("Sorry, not enough coffee!")
    elif milk_storage < milk_usage:
        print("Sorry, not enough milk!")
    elif cups_storage < cups_usage:
        print("Sorry, not enough cups!")
    else:
        print("I have enough resources, making you a coffee!")
        water_storage = water_storage - water_usage
        coffee_storage = coffee_storage - coffee_usage
        milk_storage = milk_storage - milk_usage
        money_storage = money_storage + cost
        cups_storage = cups_storage - cups_usage


def output_latte():
    calculate_usage_latte()


def calculate_usage_cappuccino():
    global water_storage
    global coffee_storage
    global milk_storage
    global money_storage
    global cups_storage
    water_usage = 200
    milk_usage = 100
    coffee_usage = 12
    cost = 6
    cups_usage = 1
    if water_storage < water_usage:
        print("Sorry, not enough water!")
    elif coffee_storage < coffee_usage:
        print("Sorry, not enough coffee!")
    elif milk_storage < milk_usage:
        print("Sorry, not enough milk!")
    elif cups_storage < cups_usage:
        print("Sorry, not enough cups!")
    else:
        print("I have enough resources, making you a coffee!")
        water_storage = water_storage - water_usage
        coffee_storage = coffee_storage - coffee_usage
        milk_storage = milk_storage - milk_usage
        money_storage = money_storage + cost
        cups_storage = cups_storage - cups_usage


def output_cappuccino():
    calculate_usage_cappuccino()


def buy_coffee():
    print("")
    choice = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: ")
    if str(choice) == "back":
        return
    if int(choice) == 1:
        output_espresso()

    if int(choice) == 2:
        output_latte()

    if int(choice) == 3:
        output_cappuccino()


def fill_ingredients():
    global water_storage
    global coffee_storage
    global milk_storage
    global money_storage
    global cups_storage
    print("")
    add_water = int(input("Write how many ml of water do you want to add: "))
    add_milk = int(input("Write how many ml of milk do you want to add: "))
    add_coffee = int(input("Write how many grams of coffee beans do you want to add: "))
    add_cups = int(input("Write how many disposable cups of coffee do you want to add: "))
    water_storage += add_water
    coffee_storage += add_coffee
    milk_storage += add_milk
    cups_storage += add_cups


def take_money():
    global money_storage
    print("")
    print("I gave you $" + str(money_storage))
    money_storage = 0


while program_is_running is True:
    print("")
    option = input("Write action (buy, fill, take, remaining, exit): ")

    if option == "buy":
        buy_coffee()
    elif option == "fill":
        fill_ingredients()
    elif option == "take":
        take_money()
    elif option == "remaining":
        show_left_ingredients()
    elif option == "exit":
        break
