"""CP1404/CP5632 Practical - Car class example."""


class Car:
    """Represent a Car object."""

    def __init__(self, name, fuel=0 ):
        """Initialise a Car instance.
        fuel: float, one unit of fuel drives one kilometre
        """
        self.name = name
        self.fuel = fuel
        self.odometer = 0

    def __str__(self):
        return "{}: fuel={}, odometer={}".format(self.name, self.fuel, self.odometer)
        #Remember that you can run this method by printing your car object,
        #or passing the car object to the str() function.

    def add_fuel(self, amount):
        """Add amount to the car's fuel."""
        self.fuel += amount

    def drive(self, distance):
        """Drive the car a given distance.
        Drive given distance if car has enough fuel
        or drive until fuel runs out return the distance actually driven.
        """
        if distance > self.fuel:
            distance = self.fuel
            self.fuel = 0
        else:
            self.fuel -= distance
        self.odometer += distance
        return distance

    def get_fuel(self):
        """Gets the fuel of the car from the Car object"""
        return self.fuel

    def get_odo(self):
        """Gets the odometer of the car from the Car object"""
        return self.odometer

    def get_name(self):
        """Gets the name of the car from the Car object"""
        return self.name