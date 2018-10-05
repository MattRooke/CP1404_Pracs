from prac_08.silver_service_taxi import SilverServiceTaxi

first_fare = SilverServiceTaxi("BMW", 100, 2)

first_fare.drive(18)

print("Expected:\nBMW, fuel=82, odometer=18, 18km on current fare, $2.46/km plus flagfall of $4.50\n"
      "Got:")
print(first_fare, "Current fare price is ${:.2f}".format(first_fare.get_fare()))

new_fare = SilverServiceTaxi("Hummer", 100, 4)

new_fare.drive(50)

print("Expected:\nHummer, fuel=50, odometer=50, 50km on current fare, $4.92/km plus flagfall of $4.50\n"
      "Got:")
print(new_fare)
