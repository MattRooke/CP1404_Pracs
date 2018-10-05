from prac_08.unreliable_car import UnreliableCar

trip_1 = UnreliableCar("Junk", 100, 40)

trip_1.drive(40)

print(trip_1)

if trip_1.get_odo() > 0:
    print("\n{} drove {}km.".format(trip_1.get_name(), trip_1.get_odo()))
else:
    print("\n{} broke down!".format(trip_1.get_name()))


