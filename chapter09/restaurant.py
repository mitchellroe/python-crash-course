#!/usr/bin/env python3


class Restaurant:
    """A restaurant.
    """

    def __init__(self, restaurant_name, cuisine_type):
        """Make a restaurant."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("This restaurant, " + self.restaurant_name
              + ", serves " + self.cuisine_type + ".")

    def open_restaurant(self):
        print(self.restaurant_name + " is now open!")
