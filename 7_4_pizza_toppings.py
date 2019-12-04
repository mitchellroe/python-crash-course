#!/usr/bin/env python3

active = 0
while active < 10:
    active += 1
    topping = input("Please enter a pizza topping or 'quit' to quit: ")
    if topping == "quit":
        break
    else:
        print("You said you wanted " + topping + " as a topping on your pizza.")
