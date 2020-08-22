# Write your code here
class CoffeeMachine:

    def __init__(self):
        self.water = 400
        self.milk = 540
        self.beans = 120
        self.cups = 9
        self.money = 550

    def remaining(self):
        print("The coffee machine has:")
        print("{0} of water".format(self.water))
        print("{0} of milk".format(self.milk))
        print("{0} of coffee beans".format(self.beans))
        print("{0} of disposable cups".format(self.cups))
        print("{0} of money".format(self.money))

    def take(self):
        print("I gave you ${0}".format(self.money))
        self.money = 0

    def fill(self):
        print("Write how many ml of water do you want to add:")
        self.water += int(self.user_input())
        print("Write how many ml of milk do you want to add:")
        self.milk += int(self.user_input())
        print("Write how many grams of coffee beans do you want to add:")
        self.beans += int(self.user_input())
        print("Write how many disposable cups of coffee do you want to add:")
        self.cups += int(self.user_input())

    def check_water(self, cup_water):
        return self.water - cup_water >= 0

    def check_milk(self, cup_milk):
        return self.milk - cup_milk >= 0

    def check_beans(self, cup_beans):
        return self.beans - cup_beans >= 0

    def check_cups(self):
        return self.cups - 1 >= 0

    def buy(self):
        print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        type_coffee = self.user_input()
        if type_coffee == "1":
            if self.check_water(250) and self.check_beans(16) and self.check_cups():
                self.water -= 250
                self.beans -= 16
                self.cups -= 1
                self.money += 4
                print("I have enough resources, making you a coffee!")
                return
            else:
                if not self.check_water(250):
                    print("Sorry, not enough water!")
                    return
                if not self.check_beans(16):
                    print("Sorry, not enough beans!")
                    return
                if not self.check_cups():
                    print("Sorry, not enough cups!")
                    return
        elif type_coffee == "2":
            if self.check_water(350) and self.check_milk(75) and self.check_beans(20) and self.check_cups():
                self.water -= 350
                self.milk -= 75
                self.beans -= 20
                self.cups -= 1
                self.money += 7
                print("I have enough resources, making you a coffee!")
                return
            else:
                if not self.check_water(350):
                    print("Sorry, not enough water!")
                    return
                if not self.check_milk(75):
                    print("Sorry, not enough milk!")
                    return
                if not self.check_beans(20):
                    print("Sorry, not enough beans!")
                    return
                if not self.check_cups():
                    print("Sorry, not enough cups!")
                    return
        elif type_coffee == "3":
            if self.check_water(200) and self.check_milk(100) and self.check_beans(12) and self.check_cups():
                self.water -= 200
                self.milk -= 100
                self.beans -= 12
                self.cups -= 1
                self.money += 6
                print("I have enough resources, making you a coffee!")
                return
            else:
                if not self.check_water(200):
                    print("Sorry, not enough water!")
                    return
                if not self.check_milk(100):
                    print("Sorry, not enough milk!")
                    return
                if not self.check_beans(12):
                    print("Sorry, not enough beans!")
                    return
                if not self.check_cups():
                    print("Sorry, not enough cups!")
                    return

    def running(self):
        while True:
            print("Write action (buy, fill, take, remaining, exit):")
            choose = self.user_input()
            print()
            if choose == "buy":
                self.buy()
            elif choose == "fill":
                self.fill()
            elif choose == "take":
                self.take()
            elif choose == "remaining":
                self.remaining()
            elif choose == "exit":
                break
            print()

    def user_input(self):
        return input()


coffee_machine = CoffeeMachine()
coffee_machine.running()
