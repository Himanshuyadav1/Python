# 1. Built-in Module / Package
# https://docs.python.org/3/py-modindex.html - Reference
"""
* math
* keywords
* random
* datetime
"""

import math

print(math.sqrt(225))
print(math.factorial(5))

import keyword

print(keyword.kwlist)
print(keyword.softkwlist)

import random

print(random.randint(1, 100))


import datetime

print(datetime.datetime.now())