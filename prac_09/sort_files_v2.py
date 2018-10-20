"""
CP1404 Practical
This is a program that takes different file types and sorts them into sub directories that the user defines.
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
    sorted_file_types = []
    document_categories = {}
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
                if doc_type not in sorted_file_types:
                    user_input_category = input("What category would you like to sort {} files into?".format(doc_type))
                    sorted_file_types.append(doc_type)
                    print("Creating {}".format(user_input_category))
                    document_categories[doc_type] = user_input_category
                    os.mkdir(user_input_category)
            except FileExistsError:
                pass
            print(document_categories)
            print("Moving {} to {}".format(filename, document_categories[doc_type]))
            try:
                shutil.move(filename, os.path.join(document_categories[doc_type], filename))
            except FileNotFoundError:
                pass

main()
