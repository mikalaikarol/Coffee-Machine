# Write your code here

# global variables

water_storage, milk_storage, coffee_storage, cups_storage, money_storage = 400, 540, 120, 9, 550
program_is_running = True


def show_left_ingredients():
    print("The coffee machine has: ")
    print(water_storage, "of water")
    print(milk_storage, "of milk")
    print(coffee_storage, "of coffee beans")
    print(cups_storage, "of disposable cups")
    print("$" + str(money_storage) + " of money")


def calculate_usage_espresso():
    global water_storage, coffee_storage, money_storage, cups_storage
    water_usage, coffee_usage, cost, cups_usage = 250, 16, 4, 1

    if water_storage < water_usage:
        print("Sorry, not enough water!")
    elif coffee_storage < coffee_usage:
        print("Sorry, not enough coffee!")
    elif cups_storage < cups_usage:
        print("Sorry, not enough cups!")
    else:
        print("I have enough resources, making you a coffee!")
        water_storage -= water_usage
        coffee_storage -= coffee_usage
        money_storage += cost
        cups_storage -= cups_usage


def calculate_usage_latte():
    global water_storage, coffee_storage, milk_storage, money_storage, cups_storage
    water_usage, milk_usage, coffee_usage, cost, cups_usage = 350, 75, 20, 7, 1

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
        water_storage -= water_usage
        coffee_storage -= coffee_usage
        milk_storage -= milk_usage
        money_storage += cost
        cups_storage -= cups_usage


def calculate_usage_cappuccino():
    global water_storage, coffee_storage, milk_storage, money_storage, cups_storage
    water_usage, milk_usage, coffee_usage, cost, cups_usage = 200, 100, 12, 6, 1

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
        water_storage -= water_usage
        coffee_storage -= coffee_usage
        milk_storage -= milk_usage
        money_storage += cost
        cups_storage -= cups_usage


def buy_coffee():
    choice = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: ")
    if choice == "back":
        return
    if choice == "1":
        calculate_usage_espresso()
    if choice == "2":
        calculate_usage_latte()
    if choice == "3":
        calculate_usage_cappuccino()


def fill_ingredients():
    global water_storage, coffee_storage, milk_storage, money_storage, cups_storage
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
    print("I gave you $" + str(money_storage))
    money_storage = 0


while program_is_running is True:
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
