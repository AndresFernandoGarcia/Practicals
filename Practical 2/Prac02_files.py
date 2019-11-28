def main():
# Names Append/Write
    namefile = open("name.txt", 'a+')
    name = input("Enter your name: ")
    namefile.write(name + "\n")
    namefile.close()
#Names Read
    namefile = open("name.txt", 'r')
    print(namefile.read())
    namefile.close()
#Numbers
    numbersfile = open("numbers.txt", 'r')
    line1 = numbersfile.readline()
    line2 = numbersfile.readline()
    result = int(line1) + int(line2)
    print(result)
    numbersfile.close()
#Numbers sum all
    numbersfile = open("numbers.txt", 'r')
    lines = numbersfile.readlines()
    total_lines = 0
    for i in lines:
        total_lines = int(i) + total_lines
    print(total_lines)
    numbersfile.close()



main()