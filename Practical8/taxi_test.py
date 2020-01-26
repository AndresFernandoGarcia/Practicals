from Practical8.taxi import Taxi

def main():
    mytaxi = Taxi("Prius 1", 100)

    mytaxi.drive(40)
    print(mytaxi , "\nCurrent fare: " , mytaxi.get_fare())
    mytaxi.start_fare()
    mytaxi.drive(100)
    print(mytaxi , "\nCurrent fare: " , mytaxi.get_fare())


main()