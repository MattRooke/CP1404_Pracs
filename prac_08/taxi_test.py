from prac_08.taxi import Taxi

first_fare = Taxi("Prius 1", 100)

first_fare.drive(40)

print("Expected:\nPrius 1, fuel=60, odometer=40, 40km on current fare, $1.23/km Current fare price is $49.20\n"
      "Got:")
print(first_fare, "Current fare price is ${:.2f}".format(first_fare.get_fare()))

new_fare = Taxi("Prius 1", 100)

new_fare.drive(100)

print("Expected:\nPrius 1, fuel=0, odometer=100, 100km on current fare, $1.23/km Current fare price is $123.00\n"
      "Got:")
print(new_fare, "Current fare price is ${:.2f}".format(new_fare.get_fare()))

