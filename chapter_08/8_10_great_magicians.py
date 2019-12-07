#!/usr/bin/env python3


def show_magicians(magicians):
    """Prints out the names of some magicians."""
    for magician in magicians:
        print(magician)


def make_great(magicians):
    """
    Makes magicians great by adding " the Great" to the end of their name.
    """
    great_magicians = []

    while magicians:
        magician = magicians.pop()
        great_magicians.append(magician + " the Great")

    while great_magicians:
        great_magician = great_magicians.pop()
        magicians.append(great_magician)


magicians = ["Larry", "Sam", "Jenna"]
show_magicians(magicians)
make_great(magicians)
show_magicians(magicians)
