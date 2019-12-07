#!/usr/bin/env python3

"""
**9-4. Number Served:** Start with your program from Exercise 9-1 (page
166).  Add an attribute called `number_served` with a default value of 0.
Create an instance called `restaurant` from this class.  Print the number of
customers the restaurant has served, and then change this value and print it
again.

Add a method called `set_number_served()` that lets you set the number of
customers that have been served.  Call this method with a new number and print
the value again.

Add a method called `increment_number_served()` that lets you increment the
number of customers who've been served.  Call this method with any number you
like that could represent how many customers were served in, say, a day of
business.
"""


class Restaurant:
    """A restaurant.
    """


    def __init__(self, restaurant_name, cuisine_type, number_served):
        """Make a restaurant."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served

    def set_number_served(self, number_served):
        self.number_served = number_served

    def describe_restaurant(self):
        print("This restaurant, " + self.restaurant_name
              + ", serves " + self.cuisine_type + ".")

    def open_restaurant(self):
        print(self.restaurant_name + " is now open!")


restaurant = Restaurant("Johnny Cakes", "pancake", 200)
print("Number served: " + str(restaurant.number_served))

print("Setting number served to 250...")
restaurant.set_number_served(250)
print("Number served: " + str(restaurant.number_served))
