total = float(0)

number_of_items = int(input("Enter the number of items: "))
while(number_of_items <= 0):
    print("Invalid number of items")
    number_of_items = int(input("Enter the number of items: "))

for i in range(0, number_of_items):
    price = float(input("Enter the price of the item: "))
    total = total + price

if(total > 100):
    discount = total * .1
    total = total - discount

print("Total price for {} items is: ${:.2f} ".format(number_of_items, total))
