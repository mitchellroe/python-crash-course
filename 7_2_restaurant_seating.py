#!/usr/bin/env python3

response = input("How many people will you have in your dinner group? ")
if int(response) > 8:
    print("I'm sorry, but you'll have to wait for a table.")
else:
    print("Your table is ready.")
