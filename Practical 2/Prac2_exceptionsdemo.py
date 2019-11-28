"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?

This error will occur when the input is the right type but an inappropriate value therefore the error appears.
If the input was dog, the int() function tries to convert the string to a number but it can't since the letters
cannot be changed into a number

2. When will a ZeroDivisionError occur?
This will occur when a number is divided by 0, since that is an undefined number it cannot be displayed.

3. Could you change the code to avoid the possibility of a ZeroDivisionError?
using a while loop to keep asking for a denominator that isn't 0

denominator = int(input("Enter the denominator: "))
while(denominator == 0)
    print("Error denominator cannot be 0")
    denominator = int(input("Enter the denominator: "))

"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")