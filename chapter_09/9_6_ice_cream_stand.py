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


class IceCreamStand(Restaurant):
    """An Ice Cream Stand, which is a type of restaurant.
    """
    def __init__(self, restaurant_name, flavors, cuisine_type="Ice Cream"):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def display_flavors(self):
        print("The flavors are: " + self.flavors)


ice_cream_stand = IceCreamStand(
    restaurant_name="Brain Freeze",
    cuisine_type="Ice Cream",
    flavors="Chocolate, Vanilla, and Swirl"
)

ice_cream_stand.display_flavors()
