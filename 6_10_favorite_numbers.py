#!/usr/bin/env python3

favorite_numbers = {
    'jeremy': [3, 7, 9],
    'phillis': [10, 4],
}

for name, numbers in favorite_numbers.items():
    print(name.title() + "'s favorite numbers are:")
    for number in numbers:
        print("\t" + str(number))
