#!/usr/bin/env python3

rivers = {
    'nile': 'egypt',
    'amazon': 'africa, I think',
}

for river, location in rivers.items():
    print("The " + river.capitalize() + " runs through "
          + location.capitalize() + ".")
