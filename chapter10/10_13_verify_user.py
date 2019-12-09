#!/usr/bin/env python3

import json

filename = 'username.json'


def get_stored_username():
    """Get stored username if available."""
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    """Prompt for a new username."""
    username = input("What is your name? ")
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    print("We'll remember you when you come back, " + username + "!")
    return username


def greet_user():
    """Greet the user by name."""
    username = get_stored_username()
    if not username:
        get_new_username()
    else:
        user_confirmation = input("Is " + username + " your username (y/N)?: ")
        if user_confirmation.lower() == 'y':
            print("Welcome back, " + username + "!")
        else:
            get_new_username()


greet_user()
