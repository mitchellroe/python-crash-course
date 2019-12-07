#!/usr/bin/env python3

"""Instantiates the ElectricCar class found in car.py."""

from electriccar import ElectricCar

my_tesla = ElectricCar('tesla', 'model s', 2016)

print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
