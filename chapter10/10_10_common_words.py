#!/usr/bin/env python3


try:
    with open("moby_dick.txt") as moby_dick:
        words = moby_dick.read()
        the_count = words.lower().count("the")
        print("The word 'the' appears in Moby Dick approximately "
              + str(the_count) + " times.")
except FileNotFoundError:
    print("Count not find moby_dick.txt")
