#!/usr/bin/env python3

while True:

    number1 = input("\nNumber 1 (or 'q' to quit): ")
    if number1 == 'q':
        break
    try:
        number1 = float(number1)
    except ValueError:
        print("Cannot convert '" + number1 + "' to a number!")
        continue

    number2 = input("Number 2 (or 'q' to quit): ")
    if number2 == 'q':
        break
    try:
        number2 = float(number2)
    except ValueError:
        print("Cannot convert '" + number2 + "' to a number!")
        continue

    value = float(number1) + float(number2)
    print("The first number, plus the second number is " + str(value))
