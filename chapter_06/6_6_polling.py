#!/usr/bin/env python3

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

who_should_take_poll = ['jen', 'jeremy', 'joshua', 'jackie']

for person in who_should_take_poll:
    if person in favorite_languages.keys():
        print("Thank you, " + person.title() + ", for taking the poll.")
    else:
        print(person.title() + ", you should take the poll!")
