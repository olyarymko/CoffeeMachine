water = 400
milk = 540
beans = 120
disposable_cups = 9
money = 550
def message():
    print("The coffee machine has:")
    print(str(water) + " of water")
    print(str(milk) + " of milk")
    print(str(beans) + " of coffee beans")
    print(str(disposable_cups) + " of disposable_cups")
    print(str(money) + " of money")
def coffee_choice():
    choice = (input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: \n"))
    global water, milk, beans, disposable_cups, money
    for i in choice:
        if choice == "1":
            water = water - 250
            beans = beans - 16
            money = money + 4
            disposable_cups = disposable_cups - 1
            print("I have enough resources, making you a coffee!")
        elif choice == "2":
            if water >= 350:
                water = water - 350
                milk = milk - 75
                beans = beans - 20
                money = money + 7
                disposable_cups = disposable_cups - 1
                print("I have enough resources, making you a coffee!")
            else:
                print("Sorry, not enough water!")
        elif choice == "3":
            water = water - 200
            milk = milk - 100
            beans = beans - 12
            money = money + 6
            disposable_cups = disposable_cups - 1
            print("I have enough resources, making you a coffee!")
        elif choice == "back":
            break
action = " "
while action != "exit":
    action = input("Write action(buy, fill, take, remaining, exit): \n")
    print(" ")
    if action == "buy":
        coffee_choice()
        print(" ")
    elif action == "fill":
        water = water + int(input("Write how many ml of water do you want to add: \n"))
        milk = milk + int(input("Write how many ml of milk do you want to add: \n"))
        beans = beans + int(input("Write how many grams of coffee beans do you want to add: \n"))
        disposable_cups = disposable_cups + int(input("Write how many disposable cups of coffee do you want to add: \n"))
        print(" ")
    elif action == "take":
        print("I gave you $" + str(money))
        money -= money
        print(" ")
    elif action == "remaining":
        message()
        print(" ")
