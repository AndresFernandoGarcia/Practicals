"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
import random

def main():
    numscores = int(input("Enter number of scores: "))
    score = 0
    for x in range(numscores):
        score = random.randint(0, 100)
        result = check_Score(score)
        print("The score is {} and the result is {}".format(score,result))

def check_Score(score):
    if score > 90:
        return("Excellent")
    elif score >= 50 :
        return("Passable")
    elif score < 50:
        return("Bad")

main()