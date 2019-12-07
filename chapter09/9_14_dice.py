#!/usr/bin/env python3

from die import Die


def roll_ten_times(die):
    for _ in range(10):
        print(die.roll_die())


die6 = Die()
roll_ten_times(die6)
print()
die10 = Die(10)
roll_ten_times(die10)
print()
die20 = Die(20)
roll_ten_times(die20)
