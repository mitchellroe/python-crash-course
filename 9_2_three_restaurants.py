#!/usr/bin/env python3

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
              + ", is a " + self.cuisine_type + " restaurant.")

    def open_restaurant(self):
        print(self.restaurant_name + " is now open!")


restaurant1 = Restaurant("Johnny Cakes", "pancake")
restaurant2 = Restaurant("Jenny Crepes", "crepe")
restaurant3 = Restaurant("Jerry Crates", "takeout")

restaurants = [restaurant1, restaurant2, restaurant3]

for restaurant in restaurants:
    restaurant.describe_restaurant()
