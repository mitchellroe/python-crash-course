#!/usr/bin/env python3

import timeit

one_million = range(1, 1000001)
print("Min: " + str(min(one_million)))
print("Max: " + str(max(one_million)))

operation = """
sum(range(1, 1000001))
"""

print("Avg time it took (n = 100) to add up 1 to 1,000,000: "
      + str(timeit.timeit(operation, number=100) / 100))
