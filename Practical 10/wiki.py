import wikipedia
import random

while True:
    try:
        search_term = input("Your term: ")
        if search_term == "":
            break

        print(wikipedia.summary(search_term, sentences=1))

    except wikipedia.exceptions.DisambiguationError as e:
        print("Your current search method is very ambiguous, therefore, I'll choose one for you at random!")
        search_term = random.choice(e.options)
        print(wikipedia.summary(search_term, sentences=1))

    except wikipedia.exceptions.PageError:
        print("page does not exist")

