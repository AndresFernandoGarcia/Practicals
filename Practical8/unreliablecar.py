from random import randint
from Practical6.car import Car

class UnreliableCar(Car):
    def __init__(self, name, fuel, reliability):
        """Initialise an UnreliableCar instance, based on parent class Car."""
        super().__init__(name, fuel)
        self. reliability = reliability

    def drive(self, distance):
        """Drive a specific range, however only if random number is greater than reliability."""
        if(self.reliability > randint(0,100)):
            distance_driven = super().drive(distance)

        else:
            distance_driven = 0
        return distance_driven
