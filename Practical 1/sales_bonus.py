"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

bonus = float(0)
sales = 0

while(sales >= 0):
    sales = float(input("Enter sales: $"))

    if(sales < 1000 and sales >= 0):#if sales lower than 1000
        bonus = sales*.10
        print("Your bonus is: ${}".format(bonus))

    elif(sales >= 1000):#if sales greater than 1000 or equal to
        bonus = sales*.15
        print("Your bonus is: ${}".format(bonus))
