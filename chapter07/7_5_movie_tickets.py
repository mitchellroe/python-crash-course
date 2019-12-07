#!/usr/bin/env python3

while True:
    age = input("Please enter your age or 'quit' to quit: ")
    if age == "quit":
        break
    elif int(age) <= 3:
        print("Your ticket is free!")
    elif int(age) > 3 and int(age) <= 12:
        print("Your ticket is $10.")
    elif int(age) > 12:
        print("Your ticket is $15.")
    else:
        print("I don't understand.  Please try again.")
