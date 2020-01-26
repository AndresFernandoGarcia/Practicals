import shutil
import os


def main():
    all_dirs = []
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
        if file_type in all_dirs:
            pass
        else:
            all_dirs.append(file_type)

    if "DS_Store" in all_dirs:
        all_dirs.remove("DS_Store")
    else:
        pass

    for file_type in all_dirs:
        try:
            os.mkdir(file_type)
        except FileExistsError:
            pass

    for filename in os.listdir('.'):
        # Ignore directories, just process files
        if os.path.isdir(filename):
            continue

        for dir_name in all_dirs:
            if dir_name == filename.split(".")[1]:
                shutil.move(filename, dir_name)


main()
