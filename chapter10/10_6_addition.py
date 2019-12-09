#!/usr/bin/env python3

number1 = input("\nPlease provide the first number: ")
number2 = input("Please provide the second number: ")
try:
    value = float(number1) + float(number2)
except ValueError:
    print("Cannot convert these to numbers!")
else:
    print("The first number, plus the second number is " + str(value))
