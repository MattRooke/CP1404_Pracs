"""
CP1404 Practical
This is a program that takes file names in a directory with multiple sub-directories and standardises them.
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

            new_name = get_fixed_filename(filename)
            print("Renaming {} to {}".format(filename, new_name))

            # Rename file to new name - in place
            os.rename(os.path.join(directory_name, filename), os.path.join(directory_name, new_name))

            # Move file to new place, with new name
            # try:
            #     os.mkdir(os.path.join(directory_name, 'temp'))
            # except FileExistsError:
            #     pass
            # shutil.move(os.path.join(directory_name, new_name), os.path.join(directory_name, 'temp/' + new_name))
            print("Moving {} to temp/{}".format(filename, new_name))


def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    words_characters = []
    new_name_characters = []
    for index, character in enumerate(filename):
        words_characters.append((index, character))
        #  Replaces lower case first letters of each word:
        if character.islower():
            previous_index, previous_character = words_characters[index - 1]
            if previous_character == " " or index == 0:  # index == 0 if first letter is lowercase.
                if character.islower():
                    character = character.upper()
                    words_characters[index] = index, character
        #  Replaces camel-caps with underscores:
        elif character.isupper():
            previous_index, previous_character = words_characters[index - 1]
            if previous_character.islower() or previous_character.isupper() and index != 0:
                previous_character = "{}_".format(previous_character)
                words_characters[previous_index] = previous_index, previous_character
    for char in range(len(words_characters)):
        new_index, new_character = words_characters[char]
        new_name_characters.append(new_character)
    new_name = "".join(new_name_characters).replace(" ", "_").replace(".T_X_T", ".txt")

    return new_name


def demo_walk():
    """Process all subdirectories using os.walk()."""
    os.chdir('Lyrics')
    for directory_name, subdirectories, filenames in os.walk('.'):
        print("Directory:", directory_name)
        print("\tcontains subdirectories:", subdirectories)
        print("\tand files:", filenames)
        print("(Current working directory is: {})".format(os.getcwd()))


main()

