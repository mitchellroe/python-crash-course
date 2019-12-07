#!/usr/bin/env python3

sandwich_orders = ["dagwood", "slim jim", "turkey", "ham", "veggie and hummus"]
finished_sandwiches = []
while sandwich_orders:
    sandwich = sandwich_orders.pop()
    finished_sandwiches.append(sandwich)
    print("I finished your " + sandwich + " sandwich.")
    
