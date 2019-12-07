#!/usr/bin/env python3

from car import Car


class Battery:
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=70):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = "This car can go approximately " + str(range)
        message += " on a full charge."
        print(message)


class AlkalineBattery(Battery):
    """
    This is a test of a subclass definition within a file that doesn't really
    name this one's superclass.
    """
    def __init__(self, brand):
        """Some stuff"""
        super().__init__()
        self.brand = brand


class ElectricCar(Car):
    """Models aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.  Then initialize attributes
        specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery = Battery()
