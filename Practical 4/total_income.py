months = int(input("Enter number of months: "))
total = 0
incomelist = []
for i in range(months):
    income = int(input("Enter income for month {}: ".format(i+1)))
    incomelist.append(income)
print("Income Report")
print("_________________")
for j in range(months):
    total = incomelist[j] + total
    print("Month {} - Income:  ${:10.2f}        Total:  ${:10.2f}".format(j+1, incomelist[j],total ))