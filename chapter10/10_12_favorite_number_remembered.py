#!/usr/bin/env python3

import json

filename = 'favorite_number.json'

"""
See if the file exists.  If it does, read the favorite number from it and
print it out to the user.  If it doesn't, then prompt the user for their
favorite number.  Store that number in a file.
"""


def read_favorite_number():
    try:
        with open(filename) as f_obj:
            favorite_number = json.load(f_obj)
        return favorite_number
    except FileNotFoundError:
        return None


def get_favorite_number():
    favorite_number = input("What is your favorite number? ")
    try:
        favorite_number = float(favorite_number)
    except ValueError:
        print("I can't convert " + favorite_number + " to a number.")
    else:
        with open(filename, 'w') as f:
            json.dump(favorite_number, f)
        print("I'll remember your favorite number next time.")


def show_favorite_number():
    favorite_number = read_favorite_number()
    if not favorite_number:
        get_favorite_number()
    else:
        print("I know your favorite number!  It's "
              + str(favorite_number) + ".")


show_favorite_number()
