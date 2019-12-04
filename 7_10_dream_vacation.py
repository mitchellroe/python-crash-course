#!/usr/bin/env python3

polling_active = True
responses = {}
while polling_active:
    name = input("\nPlease enter your name: ")
    place = input("If you could go anywhere in the world, where would it be?: ")
    responses[name] = place
    still_active = input("Are there others that would like to take the poll?: ")
    if still_active.lower() != "y":
        break

print("\nResults of the poll are in!")
for name, place in responses.items():
    print(name.title() + " would like to go to " + place + ".")
