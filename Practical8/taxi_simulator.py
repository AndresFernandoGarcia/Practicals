from Practical8.taxi import Taxi
from Practical8.silver_service_taxi import SilverServiceTaxi
# Forming taxi list
mytaxi1 = Taxi("Prius1", 100)
mytaxi2 = Taxi("Corvette", 150)
myspecialtaxi = SilverServiceTaxi("Hummer", 200, 2)
myspecialtaxi2 = SilverServiceTaxi("Ford", 250, 4)
taxi_list = [mytaxi1, mytaxi2, myspecialtaxi, myspecialtaxi2]


def main():
    total_bill = 0
    current_taxi = None
    MENU = """Menu:
     c) choose a taxi
     d) drive
     q) quit"""
    print("Let's Drive!")
    continues = True
    while (continues != False):  # loop until 'q' is pressed
        print(MENU)
        print("")
        decision = input("Enter your choice: ")

        while decision != "d" and decision != "c" and decision != "q":  # Checking if decision value is what is listed
            print("Invalid choice")
            decision = input("Enter your choice: ")

        if decision == "q":
            count = 0
            print("Cars are now: ")
            for car in taxi_list:
                count += 1
                print("{}. {}".format(count, car))
            print("Your total bill is ${}".format(total_bill))
            continues = False

        elif decision == "d":
            if current_taxi is None:  # Checking whether current_taxi has a value other than None
                print("Oops you haven't chosen a taxi yet! go do that or else...")

            else:
                drive_taxi(current_taxi)
                total_bill += get_total(current_taxi)  # Calculating total bill
                print("Total Fare: ${:.2f}".format(total_bill))
                current_taxi = None

        elif (decision == "c"):
            current_taxi = list_taxis()


def list_taxis():
    count = 0
    for car in taxi_list:
        count += 1
        print("{}. {}".format(count, car))
    finish = False
    while finish != True:  # index value error check
        print("Choose your taxi")
        try:  # try to get index input
            selection = int(input(">>> "))
            while selection < 0 or selection > len(taxi_list):
                print("Error - out of bounds")
                selection = int(input(">>> "))
            finish = True
        except ValueError:  # catches any value error in the selection value
            print("Error - index must be a number!")
    car = taxi_list[selection - 1]
    return car


def drive_taxi(taxi):
    finish = False
    while finish != True:  # index value error check
        print("How much would you want to drive?")
        try:  # try to get index input
            selection = int(input(">>> "))
            while selection < 0:
                print("Error - out of bounds")
                selection = int(input(">>> "))
            finish = True
        except ValueError:  # catches any value error in the selection value
            print("Error - index must be a number!")
    taxi.drive(selection)


def get_total(car):
    return car.get_fare()  # gets the fare of the current taxi


main()
