"""
CP1404 Practical
This is a program that takes different file types and sorts them into sub directories.
"""
import shutil
import os


def main():
    """Demo os module functions."""
    print("Starting directory is: {}".format(os.getcwd()))

    # Change to desired directory
    os.chdir('FilesToSort')

    # Print a list of all files in current directory
    print("Files in {}:\n{}\n".format(os.getcwd(), os.listdir('.')))

    # Loop through each file in the (current) directory
    doc_types = []
    # files = []
    for directory_name, subdirectories, filenames in os.walk('.'):
        for filename in filenames:
            # Ignore directories, just process files
            if os.path.isdir(filename):
                continue

            doc_name, doc_type = filename.split(".")
            # file = doc_name, doc_type
            # files.append(file)
            doc_types.append(doc_type)
            try:
                os.mkdir(doc_type)
            except FileExistsError:
                pass
            try:
                shutil.move(filename, os.path.join(doc_type, filename))
            except FileNotFoundError:
                pass

    print(doc_types)


main()
