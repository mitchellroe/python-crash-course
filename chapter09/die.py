#!/usr/bin/env python3

from random import randint


class Die:
    """Just a multi-sided die."""

    def __init__(self, sides=6):
        """Create a die with a specified number of sides."""
        self.sides = sides

    def roll_die(self):
        """Return the side that turned up during a roll."""
        return randint(1, self.sides)
