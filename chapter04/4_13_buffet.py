#!/usr/bin/env python3

foods = ('pb&j', 'cereal', 'bread', 'eggs', 'juice')
for food in foods:
    print(food)

# Should fail
# foods[0] = 'foo'

foods = ('other', 'food', 'is', 'delicious')
print("Revised menu includes:")
for food in foods:
    print(food)
