#!/usr/bin/env python3

with open("programming_poll.txt", "a") as file_object:
    while True:
        poll_response = input("Why do you like programming"
                              + " (press 'q' to quit)?: ")
        if poll_response == 'q':
            break
        else:
            file_object.write(poll_response + "\n")
