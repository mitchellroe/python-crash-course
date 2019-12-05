#!/usr/bin/env python3


def city_country(city, country):
    """Prints out a formatted city and country."""
    return(city + ", " + country)


print(city_country("Santiago", "Chile"))
print(city_country("Denver", "USA"))
print(city_country(city="Delhi", country="India"))
