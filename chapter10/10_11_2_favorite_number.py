#!/usr/bin/env python3

import json

filename = 'favorite_number.json'


def read_favorite_number():
    try:
        with open(filename) as f_obj:
            favorite_number = json.load(f_obj)
    except FileNotFoundError:
        print("I don't know your favorite number yet.")
    else:
        print("I know your favorite number!  It's " + str(favorite_number) + ".")


read_favorite_number()
