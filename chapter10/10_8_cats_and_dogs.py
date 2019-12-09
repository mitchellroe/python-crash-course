#!/usr/bin/env python3


def display_file(filename):
    try:
        with open(filename) as my_file:
            for line in my_file.readlines():
                print(line.rstrip())
    except FileNotFoundError:
        pass


display_file("cats.txt")
display_file("dogs.txt")
