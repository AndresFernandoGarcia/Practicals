def main ():
    months = int(input("Enter number of months: "))
    incomelist = []
    for i in range(months):
        income = int(input("Enter income for month {}: ".format(i+1)))
        incomelist.append(income)
    printReport(months,incomelist)


def printReport (months, incomelist):
    total = 0
    print("Income Report")
    print("_________________")
    for j in range(months):
        total = incomelist[j] + total
        print("Month {:<3}  -  Income:  ${:10.2f}        Total:  ${:10.2f}".format(j+1, incomelist[j],total ))

main()