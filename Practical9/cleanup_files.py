"""
CP1404/CP5632 Practical
Demos of various os module examples
"""
import shutil
import os


def main():
    """Demo os module functions."""
    print("Starting directory is: {}".format(os.getcwd()))

    # Change to desired directory
    os.chdir('Lyrics/Christmas')

    # Print a list of all files in current directory
    print("Files in {}:\n{}\n".format(os.getcwd(), os.listdir('.')))

    for filename in os.listdir('.'):
        # Ignore directories, just process files
        if os.path.isdir(filename):
            continue

        new_name = get_fixed_filename(filename)
        print("Renaming {} to {}".format(filename, new_name))
        os.rename(filename, new_name)


def get_fixed_filename(filename):
    special_symbols = ["(", ")", "."]
    word = ""
    """Return a 'fixed' version of filename."""
    for i, item in enumerate(filename[:-1]):
        if not item.isupper() and filename[i-1] == " ":
            word += item.upper()
        elif item == " ":
            word += "_"
        elif item in special_symbols:
            word += item
        elif not item.isupper() and filename[i+1].isupper():
            word += "{}_".format(item)
        elif item.isupper() and filename[i+1].isupper():
            word += "{}_".format(item)
        elif item.islower() and filename[i-1] is "(" or filename[i-1] is ")":
            word += item.upper()
        else:
            word += item

    new_name = word.replace(".T_X_", ".txt").replace(".tx", ".txt").replace("txtt", "txt")
    return new_name



main()
