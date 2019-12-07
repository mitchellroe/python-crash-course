#!/usr/bin/env python3

with open("guest_book.txt", "a") as guest_book:
    while True:
        guest_name = input("Please enter your name (enter 'q' to quit): ")
        if guest_name == 'q':
            break
        else:
            print("Your name is " + guest_name + ", and you have been added to"
                  + " the guest book.")
            guest_book.write(guest_name + "\n")
