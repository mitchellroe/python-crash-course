#!/usr/bin/env python3

"""
Test to see whether a subclass defined in the same file as its superclass
can be imported directly.  The answer, at least with my version of Python, is
no.  This should fail.

To give some background, battery.py defines a couple of classes, Battery and
AlkalineBattery, which is a subclass of Battery.  AlkalineBattery cannot be
imported directly.
"""

from battery import AlkalineBattery

my_battery = AlkalineBattery("Duracell")
print(str(my_battery.brand))
