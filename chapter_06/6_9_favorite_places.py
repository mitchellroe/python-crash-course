#!/usr/bin/env python3

favorite_places = {
    'jeremy': 'milan',
    'phillis': 'berlin',
}

for name, place in favorite_places.items():
    print(name.title() + "'s favorite place is " + place.title() + ".")
