def main():
    average = 0
    numberlist = []
    for i in range(5):
        number = int(input("Enter number>>> "))
        numberlist.append(number)

    print("first number is {}".format(numberlist[0]))
    print("The last number is {}".format(numberlist[-1]))
    numberlist.sort()
    print("The smallest number is {}".format(numberlist[0]))
    print("The largest number is {}".format(numberlist[-1]))
    for i in range(5):
        average += numberlist[i]

    average = average/5
    print("The total is {}".format(average))

    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface',
                 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer',
                 'bob']

    username = input("Enter your username: ")

    granted = False
    for item in usernames:
        if(username == item):
            print("Access Granted")
            granted = True
    if(granted == False):
        print("Access Denied")




main()