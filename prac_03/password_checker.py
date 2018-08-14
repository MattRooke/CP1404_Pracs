""""Matthew Rooke"""

MIN_LENGTH = 5


def main():
    password = get_password()
    print_hidden_length(password)


def print_hidden_length(password):
    for character in range(len(password)):
        print("*", end="")


def get_password():
    password = input("Enter your password:")
    while len(password) < MIN_LENGTH:
        password = input("Enter a password {} characters long:".format(MIN_LENGTH))
    return password


main()