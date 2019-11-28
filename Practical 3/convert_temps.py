
tempsfile = open("temps_input.txt", 'r')
outfile = open ("temps_out.txt", 'a+')
lines = tempsfile.readlines()
for i in lines:
    fahrenheit = i
    celsius = 5 / 9 * (float(fahrenheit) - 32)
    outfile.write(str(celsius)+ "\n")
tempsfile.close()
outfile.close()

