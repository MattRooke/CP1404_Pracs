""" Simple menu-driven program """

def main():
    name = input("What is your name? :")
    choice = ""
    menu = """
(H)ello
(G)oodbye
(Q)uit
    """
    while choice != "Q":
        print(menu)
        choice = input(">>>").upper()
        if choice == "H":
            print("hello", name)
        elif choice == "G":
            print("Goodbye", name)
        elif choice != "Q":
            print("Invalid menu choice")
    print("Finished!")


main()
