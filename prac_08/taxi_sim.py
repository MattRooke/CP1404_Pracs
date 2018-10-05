"""Prac_08 Taxi simulation"""

from prac_08.taxi import Taxi
from prac_08.silver_service_taxi import SilverServiceTaxi

AVAILABLE_TAXIS = [Taxi("Prius", 100), Taxi("Van", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi(
    "Rolls-Royce", 100, 5)]


def main():
    current_taxi = None
    bill = 0.00
    menu_selection = ""
    while menu_selection != "q":
        menu_selection = input("q)uit, c)hoose taxi, d)rive\n>>>").lower()
        while menu_selection not in ["q", "c", "d"]:
            print("Invalid menu choice...")
            menu_selection = input("q)uit, c)hoose taxi, d)rive\n>>>").lower()
        if menu_selection == "c":
            current_taxi = choose_taxi()
            print("Bill to date: ${:.2f}".format(bill))
        elif menu_selection == "d":
            if current_taxi:
                bill += drive_taxi(current_taxi)
                print("Bill to date: ${:.2f}".format(bill))
            else:
                print("Please Select a taxi first!")
    print("Total trip cost: ${:.2f}\nTaxis are now:".format(bill))
    list_taxis()


def choose_taxi():
    print("Taxis Available:")
    list_taxis()
    user_input_selected_taxi = ""
    while user_input_selected_taxi not in range(len(AVAILABLE_TAXIS)):
        try:
            user_input_selected_taxi = int((input("Choose taxi:")))
            if user_input_selected_taxi not in range(len(AVAILABLE_TAXIS)):
                print("Sorry that taxi is unavailable.")
        except ValueError:
            print("Sorry that taxi is unavailable.")

    selected_taxi = AVAILABLE_TAXIS[user_input_selected_taxi]
    return selected_taxi


def list_taxis():
    for taxi in range(len(AVAILABLE_TAXIS)):
        print("{} -".format(taxi), AVAILABLE_TAXIS[taxi])


def drive_taxi(current_taxi):
    user_input_distance = int(input("Drive how far? "))
    current_taxi.current_fare_distance = 0  # set to 0 for each new fare
    current_taxi.drive(user_input_distance)
    trip_cost = current_taxi.get_fare()
    print("Your {} trip cost you ${:.2f}".format(current_taxi.get_name(), current_taxi.get_fare()))
    return trip_cost


main()
