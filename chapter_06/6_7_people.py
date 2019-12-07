#!/usr/bin/env python3

friend_1 = {
    'first_name': 'joe',
    'last_name': 'schmo',
    'city': 'los angeles'
}

friend_2 = {
    'first_name': 'phil',
    'last_name': 'manning',
    'city': 'springfield',
}

friend_3 = {
    'first_name': 'mary',
    'last_name': 'contrary',
    'city': 'kingston',
}

friends = [friend_1, friend_2, friend_3]

for friend in friends:
    print(friend['first_name'].title() + " " + friend['last_name'].title() + " lives in " + friend['city'].title())
