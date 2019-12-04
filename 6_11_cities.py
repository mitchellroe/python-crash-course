#!/usr/bin/env python3

cities = {
    'milan': {
        'country': 'italy',
        'population': 17000,
        'fact': "it's a beautiful place to visit",
    },
    'berlin': {
        'country': 'germany',
        'population': 10000000,
        'fact': "it used to be divided by the berlin wall",
    },
    'amsterdam': {
        'country': 'the netherlands',
        'population': 2,
        'fact': "before the nuclear winter, this place was filled with people.",
    },
}

for city, information in cities.items():
    print(city.title() + ":")
    for attribute, value in information.items():
        print(str(attribute).title() + ": " + str(value).capitalize())
    print()
