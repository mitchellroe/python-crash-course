#!/usr/bin/env python3

with open('learning_python.txt') as file_object:
    for line in file_object:
        message = line.replace('Python', 'C').rstrip()
        print(message)
