#!/usr/bin/env python3


def make_shirt(size="Large", text="I love Python"):
    """Makes a shirt, or at least tells you about it."""
    print("I'll be making a " + size + " shirt with '" + text + "' written on"
          + " the front of it.")


make_shirt(size="Medium")
make_shirt()
make_shirt(text="This is another message!")
