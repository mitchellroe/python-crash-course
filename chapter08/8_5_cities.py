#!/usr/bin/env python3


def describe_city(city, country="USA"):
    print(city.title() + " is in " + country)


describe_city("Reykjavik", "Iceland")
describe_city(city="Chicago")
describe_city("Denver")
