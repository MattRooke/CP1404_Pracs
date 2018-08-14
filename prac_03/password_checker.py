""""Matthew Rooke"""

MIN_LENGTH = 5


def main():
    password = input("Enter your password:")
    while len(password) < MIN_LENGTH:
        password = input("Enter a password {} characters long:".format(MIN_LENGTH))
    for character in range(len(password)):
        print("*", end="")


main()