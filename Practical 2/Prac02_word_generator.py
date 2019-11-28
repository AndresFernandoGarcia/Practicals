"""
CP1404/CP5632 - Practical
Random word generator - based on format of words
Another way to get just consonants would be to use string.ascii_lowercase
(all letters) and remove the vowels.
"""
import random

VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"
#word_format = "ccvcvvc"
word_format = input("Enter your word format(# = consonant, % = vowel): ")
word_format = word_format.replace(" ", "")
errorcounter = 0

"""
while(exit != True): #checks if word format contains c and v
    for kind in word_format:
        if (kind != "c" and kind != "v"):
            errorcounter += 1

    if (errorcounter == 0):
        exit = True

    elif(errorcounter > 0):
        print("Error-word format contains characters other than c or v")
        word_format = input("Enter your word format(c = consonant, v = vowel): ")
        word_format.replace(" ", "")
        errorcounter = 0
        exit = False
"""

word_format.lower()
word = ""
for kind in word_format:
    if kind == "#":
        word += random.choice(CONSONANTS)
    elif kind == "%":
        word += random.choice(VOWELS)
    else:
        word += kind

print(word)