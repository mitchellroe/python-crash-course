#!/usr/bin/env python3

# 2-7. Stripping Names: Store a person's name, and include some whitespace
# characters at the beginning and end for the name.  Make sure you use each
# character combination, "\t" and "\n", at least once.
#
# Print the name once, so the whitespace around the name is displayed.  Then
# print the name using each of the three stripping functions, lstrip(),
# rstrip(), and strip().

my_name = " mitchell \n roe \t  "
print(my_name.lstrip())
print(my_name.rstrip())
print(my_name.strip())
