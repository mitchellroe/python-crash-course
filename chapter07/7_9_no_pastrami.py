#!/usr/bin/env python3

sandwich_orders = ["dagwood", "pastrami", "slim jim", "turkey", "pastrami",
                   "ham", "veggie and hummus", "pastrami"]
finished_sandwiches = []
print("The deli is out of pastrami.")

while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    finished_sandwiches.append(sandwich)
    print("I finished your " + sandwich + " sandwich.")
