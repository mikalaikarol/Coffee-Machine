# Write your code here
water_per_cup = 200
milk_per_cup = 50
coffee_per_cup = 15

water_storage = int(input("Write how many ml of water the coffee machine has: "))
milk_storage = int(input("Write how many ml of milk the coffee machine has: "))
coffee_storage = int(input("Write how many grams of coffee beans the coffee machine has: "))
max_cups_possible = min(water_storage // water_per_cup, milk_storage // milk_per_cup, coffee_storage // coffee_per_cup)
cups_needed = int(input("Write how many cups of coffee you will need: "))
extra_cups = max_cups_possible - cups_needed

if max_cups_possible == cups_needed:
    print("Yes, I can make that amount of coffee")
elif extra_cups > 0:
    print("Yes, I can make that amount of coffee (and even", extra_cups, "more than that)")
elif cups_needed > max_cups_possible:
    print("No, I can make only", max_cups_possible, "cups of coffee")

option = input("Write action (buy, fill, take): ")


def show_left_ingredients():
    print("The coffee machine has: ")
    print(water_storage + "")
    print(milk_storage + "of milk")
    print(coffee_storage + "of coffee beans")
    # add cups number
    # add money number


def calculate_usage_espresso():
    global water_storage
    global coffee_storage
    water_usage = 250
    coffee_usage = 16
    water_storage = water_storage - water_usage
    coffee_storage = coffee_storage - coffee_usage


def output_espresso():
    calculate_usage_espresso()
    show_left_ingredients()


def calculate_usage_latte():
    global water_storage
    global coffee_storage
    global milk_storage
    water_usage = 350
    milk_usage = 75
    coffee_usage = 20
    water_storage = water_storage - water_usage
    coffee_storage = coffee_storage - coffee_usage
    milk_storage = milk_storage - milk_usage


def output_latte():
    calculate_usage_latte()
    show_left_ingredients()


def calculate_usage_cappuccino():
    global water_storage
    global coffee_storage
    global milk_storage
    water_usage = 200
    milk_usage = 100
    coffee_usage = 12
    water_storage = water_storage - water_usage
    coffee_storage = coffee_storage - coffee_usage
    milk_storage = milk_storage - milk_usage


def output_cappuccino():
    calculate_usage_cappuccino()
    show_left_ingredients()


def add_money():
    pass


def buy_coffee():
    espresso = 1
    latte = 2
    cappuccino = 3
    choice = int(input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:"))
    if choice == 1:
        output_espresso()
        add_money()
    if choice == 2:
        output_latte()
        add_money()
    if choice == 3:
        output_cappuccino()
        add_money()


if option == "buy":
    buy_coffee()
elif option == "fill":
    fill_ingridients()
elif option == "take":
    take_money()
