from Practical8.taxi import Taxi

def main():
    mytaxi = Taxi("Prius 1", 100)

    mytaxi.drive(40)
    print(mytaxi)
    mytaxi.start_fare()
    print(mytaxi)


main()