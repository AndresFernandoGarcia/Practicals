import random

numberlist = []
select = int(input("number>>> "))
MAX = 49
MIN = 1
number = 0

for i in range(select):
    for j in range(1,7):
        number = random.randint(MIN,MAX)
        for item in numberlist:
            while(number == item):
                number = random.randint(MIN,MAX)
        numberlist.append(number)
    numberlist.sort()
    print(numberlist)
    numberlist = []






