from prac_08.car import Car
import random

class UnreliableCar(Car):
    """Special version of car that includes unreliability"""
    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive the car a given distance. Given its reliability is greater than a random number.

        Drive given distance if car has enough fuel
        or drive until fuel runs out return the distance actually driven.
        """
        if self.reliability > random.randrange(0, 100):
            if distance > self.fuel:
                distance = self.fuel
                self.fuel = 0
            else:
                self.fuel -= distance
            self.odometer += distance
        else:
            distance = 0
        return distance
