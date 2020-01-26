import shutil
import os


def main():
    dirs_dictionary = {}  # Directories Dictionary with categories
    cats = []  # Categories
    print("Starting directory is: {}".format(os.getcwd()))

    # Change to desired directory
    os.chdir('FilesToSort')

    # Print a list of all files in current directory
    print("Files in {}:\n{}\n".format(os.getcwd(), os.listdir('.')))

    for filename in os.listdir('.'):
        # Ignore directories, just process files
        if os.path.isdir(filename):
            continue
        file_type = filename.split(".")[1]
        if file_type == "DS_Store":
            continue
        else:
            dirs_dictionary[file_type] = None

    for filetype in dirs_dictionary:  # Adding categories to each
        category = str(input("What category would you like to sort {} files into?".format(filetype)))
        category = category.lower().capitalize()
        dirs_dictionary[filetype] = category
        cats.append(category)

    for file_type in cats:
        try:
            os.mkdir(file_type)
        except FileExistsError:
            pass

    for filename in os.listdir('.'):
        # Ignore directories, just process files
        if os.path.isdir(filename):
            continue

        for file_t, dir_name in dirs_dictionary.items():
            if file_t == filename.split(".")[1]:
                shutil.move(filename, dir_name)



main()