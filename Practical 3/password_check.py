def main():
    password = input("Enter password: ")
    newpassword = get_Password(password)
    print (newpassword)

def get_Password(password):
    newpassword = ""
    for star in range (len(password)):
        newpassword = newpassword + "*"

    return newpassword

main()


