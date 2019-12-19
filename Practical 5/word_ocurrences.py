def main():
    string = input("enter>>> ")
    string = string.lower()
    word_dictionary = {}
    word_list = string.split()
    word_list.sort()
    for word in word_list:
        if word not in word_dictionary:
            word_dictionary[word] = word_list.count(word)

    for key,value in word_dictionary.items():
        print("{:{}} : {}".format(key, 5, value))



main()
