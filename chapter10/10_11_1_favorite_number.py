#!/usr/bin/env python3

import json


def get_favorite_number():
    favorite_number = input("What is your favorite number?: ")
    try:
        favorite_number = float(favorite_number)
    except ValueError:
        print("Cannot convert " + favorite_number + " to a number!")
        return None
    else:
        return favorite_number


def store_favorite_number():
    favorite_number = get_favorite_number()
    if favorite_number:
        with open('favorite_number.json', 'w') as f_obj:
            json.dump(favorite_number, f_obj)
        print("Stored your favorite number for next time.")
    else:
        print("No favorite number provided, so not storing anything.")


store_favorite_number()
