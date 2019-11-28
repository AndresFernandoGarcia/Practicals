for i in range(1, 23, 2):
    print(i, end=' ')
print()

for i in range(0, 110, 10):
    print(i, end=' ')
print()

for i in range(20, 0, -1):
    print(i, end=' ')
print()

stars = int(input("Enter number of stars: "))
for i in range(stars):
    print("*", end=" ")
print()

for i in range(0,stars):
    for j in range(0, i+1):
        print("*",end="")
    print("\r")


