import os


def main():
    print("Starting directory is: {}".format(os.getcwd()))

    # Change to desired directory
    os.chdir('Lyrics/Christmas')

    # Print a list of all files in current directory
    print("Files in {}:\n{}\n".format(os.getcwd(), os.listdir('.')))

    for filename in os.listdir('.'):
        # Ignore directories, just process files
        if os.path.isdir(filename):
            continue

        #read
        text_file = open(filename, "a")
        text_file.write("\n.i (c) 2011 Thankyou Music (Admin. by Crossroad Distributors Pty. Ltd.)")
        text_file.close()

main()
