#!/usr/bin/env python3

turbo = {
    'type': 'cat',
    'owner': 'will',
}

snowball = {
    'type': 'dog',
    'owner': 'jeremiah',
}

pets = [turbo, snowball]

for pet in pets:
    for key, value in pet.items():
        print(key + ": " + value)
