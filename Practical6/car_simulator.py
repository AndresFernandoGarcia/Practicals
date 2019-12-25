from Practical6.car import Car

def main():
    MENU = """Menu:
 d) drive
 r) refuel
 q) quit"""
    print("Let's Drive!")
    name = input("Enter your car name: ")
    my_car = Car(name,100)

    continues = True
    while(continues != False):
        print("")
        print(my_car)
        print(MENU)
        decision = input("Enter your choice: ")

        while(decision != "d" and decision != "r" and decision != "q"):
            print("Invalid choice")
            decision = input("Enter your choice: ")

        if(decision == "q"):
            continues = False
            print("Goodbye {}'s driver".format(my_car.get_name()))

        elif (decision == "d"):
            drive_car(my_car)

        elif (decision == "r"):
            add_carfuel(my_car)

def drive_car(car):
    """Uses object car and drives x kilometres using Car class"""
    distance = int(input("How many km do you wish to drive?: "))

    while (distance < 0):
        print("distance must be >= 0")
        distance = int(input("How many km do you wish to drive?: "))

    if(car.get_fuel() < distance):
        print("The car drove {}km and ran out of fuel.".format(car.get_fuel()))

    else:
        print("The car drove {}km".format(distance))

    car.drive(distance)




def add_carfuel(car):
    """Uses object car and adds fuel using Car class"""
    amount = int(input("How many units of fuel do you want to add to the car?: "))
    while (amount < 0):
        print("Fuel amount must be >= 0")
        amount = int(input("How many units of fuel do you want to add to the car?: "))

    print("added {} units of fuel".format(amount))
    car.add_fuel(amount)











if __name__ == '__main__':
    main()