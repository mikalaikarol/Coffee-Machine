# Write your code here


water_storage = 400
milk_storage = 540
coffee_storage = 120
cups_storage = 9
money_storage = 550


def show_left_ingredients():
    print("The coffee machine has: ")
    print(water_storage, "of water")
    print(milk_storage, "of milk")
    print(coffee_storage, "of coffee beans")
    print(cups_storage, "of disposable cups")
    print(money_storage, "of money")


def calculate_usage_espresso():
    global water_storage
    global coffee_storage
    global money_storage
    global cups_storage
    water_usage = 250
    coffee_usage = 16
    cost = 4
    water_storage = water_storage - water_usage
    coffee_storage = coffee_storage - coffee_usage
    money_storage = money_storage + cost
    cups_storage = cups_storage - 1


def output_espresso():
    calculate_usage_espresso()
    show_left_ingredients()


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
    water_storage = water_storage - water_usage
    coffee_storage = coffee_storage - coffee_usage
    milk_storage = milk_storage - milk_usage
    money_storage = money_storage + cost
    cups_storage = cups_storage - 1


def output_latte():
    calculate_usage_latte()
    show_left_ingredients()


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
    water_storage = water_storage - water_usage
    coffee_storage = coffee_storage - coffee_usage
    milk_storage = milk_storage - milk_usage
    money_storage = money_storage + cost
    cups_storage = cups_storage - 1


def output_cappuccino():
    calculate_usage_cappuccino()
    show_left_ingredients()


def buy_coffee():
    choice = int(input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino: "))
    if choice == 1:
        output_espresso()

    if choice == 2:
        output_latte()

    if choice == 3:
        output_cappuccino()


def fill_ingredients():
    global water_storage
    global coffee_storage
    global milk_storage
    global money_storage
    global cups_storage

    add_water = int(input("Write how many ml of water do you want to add: "))
    add_milk = int(input("Write how many ml of milk do you want to add: "))
    add_coffee = int(input("Write how many grams of coffee beans do you want to add: "))
    add_cups = int(input("Write how many disposable cups of coffee do you want to add: "))
    water_storage = water_storage + add_water
    coffee_storage = coffee_storage + add_coffee
    milk_storage = milk_storage + add_milk
    cups_storage = cups_storage + add_cups
    show_left_ingredients()


def take_money():
    pass


show_left_ingredients()
option = input("Write action (buy, fill, take): ")

if option == "buy":
    buy_coffee()
elif option == "fill":
    fill_ingredients()
elif option == "take":
    take_money()
