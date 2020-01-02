from Practical6.guitar import Guitar


guitar_list = []
guitar_list.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
guitar_list.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

def main():

    continues = False
    while (continues != True):
        user_input = input("Enter name of guitar: ")
        user_input = user_input.upper()


        if(user_input == ""):
            continues = True

        else:
            get_details(user_input)
    count = 1
    print("\nThese are my guitars!")
    for item in guitar_list:
        count += 1

        if (item.is_vintage() == True):
            print("Guitar {} : {}({}), worth ${} (vintage)".format(count, item.get_name(), item.get_year(), item.get_cost()))

        else:
            print("Guitar {} : {}({}), worth ${}".format(count, item.get_name(),item.get_year(), item.get_cost()))



def get_details(name):
    """Inputted name and gets year and the cost of guitar to append into list"""
    year = int(input("Enter the year>>> "))
    cost = float(input("Enter the cost if the guitar>>> "))

    field = name,year,cost

    guitar_list.append(field)





if __name__ == '__main__':
    main()