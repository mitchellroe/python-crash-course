#!/usr/bin/env python3

name = input("Please provide your name: ")

with open("guest.txt", "w") as file_object:
    file_object.write(name)
