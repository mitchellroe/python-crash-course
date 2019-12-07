#!/usr/bin/env python3

with open('learning_python.txt') as file_object:
    print(file_object.read())

with open('learning_python.txt') as file_object:
    for line in file_object:
        print(line.rstrip())

lines = []
with open('learning_python.txt') as file_object:
    lines = file_object.readlines()

print()
for line in lines:
    print(line.rstrip())
