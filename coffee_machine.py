class CoffeeMachine:
    def __init__(self, water, milk, beans, disposable_cups, money):
        self.water = water
        self.milk = milk
        self.beans = beans
        self.disposable_cups = disposable_cups
        self.money = money
        self.state = None
        self.choice = None
    def machine_state(self):
        while self.state != "exit":
            self.state = input("Write action(buy, fill, take, remaining, exit): \n")
            if self.state == "buy":
                print(" ")
                return CoffeeMachine.coffee_choice(self)
            elif self.state == "fill":
                self.water += int(input("Write how many ml of water do you want to add: \n"))
                self.milk += int(input("Write how many ml of milk do you want to add: \n"))
                self.beans += int(input("Write how many grams of coffee beans do you want to add: \n"))
                self.disposable_cups += int(input("Write how many disposable cups of coffee do you want to add: \n"))
                print(" ")
            elif self.state == "take":
                print("I gave you $" + str(self.money))
                self.money -= self.money
                print(" ")
            elif self.state == "remaining":
                print("The coffee machine has: \n {} of water \n {} of milk \n {} of coffee beans"
                      "\n {} of disposable_cups \n {} of money".format(self.water,
                                                                       self.milk,
                                                                       self.beans,
                                                                       self.disposable_cups,
                                                                       self.money))
                print(" ")
            elif self.state == "exit":
                break
    def coffee_choice(self):
        self.choice = (input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: \n"))
        if self.choice == "1":
            self. water -= 250
            self.beans -= 16
            self.money += 4
            self.disposable_cups -= 1
            print("I have enough resources, making you a coffee!")
            print(" ")
            CoffeeMachine.machine_state(self)
        elif self.choice == "2":
            if self.water >= 350:
                self. water -= 350
                self.milk -= 75
                self.beans -= 20
                self.money += 7
                self.disposable_cups -= 1
                print("I have enough resources, making you a coffee!")
                print(" ")
                CoffeeMachine.machine_state(self)
            else:
                print("Sorry, not enough water!")
                print(" ")
                CoffeeMachine.machine_state(self)
        elif self.choice == "3":
            self. water -= 200
            self.milk -= 100
            self.beans -= 12
            self.money += 6
            self.disposable_cups -= 1
            print("I have enough resources, making you a coffee!")
            print(" ")
            CoffeeMachine.machine_state(self)
        elif self.choice == "back":
            print(" ")
            CoffeeMachine.machine_state(self)

machine = CoffeeMachine(400, 540, 120, 9, 550)

machine.machine_state()

