#!/usr/bin/env python3


def make_shirt(size, text):
    """Makes a shirt, or at least tells you about it."""
    print("I'll be making a " + size + " shirt with '" + text + "' written on"
          + " the front of it.")


make_shirt("M", "My shirt is cooler than yours.")
make_shirt(size="L", text="This shirt is bigger.")
