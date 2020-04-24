water = int(input("Write how many ml of water the coffee machine has: > "))
milk = int(input("Write how many ml of milk the coffee machine has: > "))
beans = int(input("Write how many grams of coffeee beans the coffee machine has: > "))
cups = int(input("Write how many cups of coffee you will need: > "))
min_water = 200
min_milk = 50
min_beans = 15
amount_water = water//min_water
amount_milk = milk//min_milk
amount_beans = beans//min_beans
amount = [amount_water, amount_milk, amount_beans]
min_cups = min(amount)
if cups == min_cups:
    print("Yes, I can make that amount of coffee")
elif cups > min_cups:
    print("No, I can make only " + str(min_cups) + " cups of coffee")
elif cups < min_cups:
    result_cups = min_cups - cups
    print("Yes, I can make that amount of coffee (and even " + str(result_cups) + " more than that)")




