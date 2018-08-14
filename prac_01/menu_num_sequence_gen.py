"""
A simple menu-driven number sequence generator
that can:
Show the even numbers from x to y
Show the odd numbers from x to y
Show the squares from x to y
Exit the program
"""

import math

def main():
    x = int(input("x ="))
    y = int(input("y ="))
    selection = " "
    while selection != "e":
        print("\n(1)Show the even numbers from", x, "to", y, "\n"
              "(2)Show the odd numbers from", x, "to", y, "\n"
              "(3)Show the squares from", x, "to", y, "\n"
              "(E)xit")
        selection = input(">").lower()
        if selection == "1":
            for i in range(x, y + 1):
                num = i % 2
                if num == 0:
                    print(i, end=" ")
        elif selection == "2":
            for i in range(x, y + 1):
                num = i % 2
                if num == 1:
                    print(i, end=" ")
        elif selection == "3":
            for i in range(x, y + 1):
                num = math.sqrt(i) % 1
                if num == 0:
                    print(i, end=" ")
        elif selection != "e":
            print("Invalid menu selection!")
    print("Finished!")


main()
