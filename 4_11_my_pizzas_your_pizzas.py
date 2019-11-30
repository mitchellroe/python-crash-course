#!/usr/bin/env python3

pizzas = ['cheese', 'arugula', 'vegan']
# The example in the book is to use a slice, i.e. `friend_pizzas = pizzas[:]`.
# This produces a syntax error for me.
friend_pizzas = pizzas.copy()
pizzas.append('kale')
friend_pizzas.append('pepperoni')
print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)
print("My friends favorite pizzas are:")
for friend_pizza in friend_pizzas:
    print(friend_pizza)
