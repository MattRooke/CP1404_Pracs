"""prac_06 extension: car driving simulator"""

from prac_08.car import Car


def main():
    user_name = input("Let's drive!\nEnter your car name:")
    car = Car(user_name, 100)

    menu_selection = ""
    while menu_selection != "q":
        print(car)
        menu_selection = menu("Menu:\nd) drive\nr) refuel\nq) quit")
        if menu_selection == "d":
            drive(car)
        elif menu_selection == "r":
            refuel(car)
    print("Good bye {}'s driver.".format(user_name))


def refuel(car):
    refuel_amount = 0
    while refuel_amount < 1:
        try:
            refuel_amount = int(input("How many units of fuel do you want to add to the car?"))
            if refuel_amount < 1:
                print("Fuel amount must be >= 0")
        except ValueError:
            print("Invalid entry.")
    car.add_fuel(refuel_amount)
    print("Added {} units of fuel\n".format(refuel_amount))


def drive(car):
    distance_to_drive = ""
    while distance_to_drive == "":
        try:
            starting_odo = car.get_odo()
            distance_to_drive = int(input("How many km do you wish to drive?"))
            if distance_to_drive < 1:
                distance_to_drive = ""
                print("Distance must be >= 0")
            else:
                car.drive(distance_to_drive)
                distance_driven = car.get_odo() - starting_odo
                if car.get_fuel() == 0:
                    fuel_string = " and ran out of fuel."
                else:
                    fuel_string = "."
                print("The car drove {}km{}\n".format(distance_driven, fuel_string))
        except ValueError:
            print("Invalid entry.")


def menu(ui):
    """Displays a user interface and returns choice, with incorrect input handling"""
    print(ui)
    menu_selection = input("Enter your choice:").lower()
    while menu_selection not in ["d", "r", "q"]:
        print("Invalid menu choice\n")
        print(ui)
        menu_selection = input("Enter your choice:").lower()
    return menu_selection


main()
