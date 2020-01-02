from Practical6.guitar import Guitar

def main():
    gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
    another_guitar = Guitar("Another Guitar", 2013, 6)
    guitar_list = [gibson, another_guitar]

    trueanswer = gibson.get_age()
    trueanswer2 = another_guitar.get_age()
    trueanswer3 = gibson.is_vintage()
    trueanswer4 = another_guitar.is_vintage()

    print("Gibson L-5 CES get_age() - Expected 97. Got {}".format(trueanswer))
    print("Another Guitar get_age() - Expected 6. Got {}".format(trueanswer2))
    print("Gibson L-5 CES is_vintage() - Expected True. Got {}".format(trueanswer3))
    print("Another Guitar is_vintage() - Expected False. Got {}".format(trueanswer4))


if __name__ == '__main__':
    main()