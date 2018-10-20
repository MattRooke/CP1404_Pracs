"""
CP1404 Practical
This is a program that looks at files in a directory with multiple sub-directories and find if they are missing any
information.
"""
import shutil
import os


def main():
    """Demo os module functions."""
    print("Starting directory is: {}".format(os.getcwd()))

    # Change to desired directory
    os.chdir('Lyrics')

    # Print a list of all files in current directory
    print("Files in {}:\n{}\n".format(os.getcwd(), os.listdir('.')))

    # Loop through each file in the (current) directory
    for directory_name, subdirectories, filenames in os.walk('.'):
        for filename in filenames:
            # Ignore directories, just process files

            if os.path.isdir(filename):
                continue

            open_file = open(os.path.join(directory_name, filename), 'r+')
            file_lines = open_file.readlines()
            joined_lines = " ".join(file_lines)
            if '.i (c)' in joined_lines or ".i ©" in joined_lines:
                print(directory_name, filename)


main()
