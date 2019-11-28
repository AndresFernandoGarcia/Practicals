"""
What did you see on line 1?
 What was the smallest number you could have seen, what was the largest?

 Prints a number between 5 to 20, the smallest number possible is 5 and largest is 20.

 What did you see on line 2?
 What was the smallest number you could have seen, what was the largest?
 Could line 2 have produced a 4?

 smallest number would be 3, and largest 9.
 The function is designed to print a random number between a specific range but only numbers that have a 2 number difference
 in between eacother, so in this case 3,5,7 or 9. Therefore, 4 wouldn't be possible with these parameters.

 What did you see on line 3?
 What was the smallest number you could have seen, what was the largest?

 Printing a number from 2.5 from 5.5 but allows decimal numbers.
 Smallest number would be 2.5, and Largest 5.5.
"""






import random
print(random.randint(5, 20))  # line 1 printing a number from 5 to 20
print(random.randrange(3, 10, 2))  # line 2 Printing a number between 3 and 10 but only 2 numbers apart so either 3,5,7 or 9
print(random.uniform(2.5, 5.5))  # line 3 Printing a number from 2.5 from 5.5 but allows decimal numbers