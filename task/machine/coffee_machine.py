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
