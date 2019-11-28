import string

def main():
    yourstring = input("Enter thy string: ")
    checkString(yourstring)

def checkString(ourString):
    count = 0
    for char in ourString:
       if char.lower() in string.ascii_letters:
            count += 1

    print (count)

main()