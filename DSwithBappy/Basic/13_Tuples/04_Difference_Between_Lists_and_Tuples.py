"""
Difference between Lists and Tuples

* Syntax - list [], tuple ()
* Mutability - list is mutable and tuple is immutable
* Speed - list is little bit slow than tuple. In Python whatever immutable data types you have, it is a little bit fast than the mutable one.
* Memory - Tuple takes usually less space than List
* Built in functionality - Built in functionality wise list have more built in functionality because list is mutable on other hand tuple have only 2 built in functionality
* Error prone
* Usability - If you want to change anything use list and if you don't want to change anything use tuple
"""

print('Creating List and Tuple using range')
print(range(5)) # range(0, 5)
print(list(range(5))) # [0, 1, 2, 3, 4]
print(tuple(range(5))) # (0, 1, 2, 3, 4)

print()

# Memory test
print('Memory test')

import sys

L = list(range(1000))
T = tuple(range(1000))

print('List size', sys.getsizeof(L)) # 8056
print('Tuple size', sys.getsizeof(T)) # 8040

print()

# Error prone
print('Error prone')
print('List')

a = [1, 2, 3]
b = a

a.append(4)

print(a) # [1, 2, 3, 4]
print(b) # [1, 2, 3, 4]

print()

print('Tuple')

a = (1, 2, 3)
b = a

a = a + (4,)

print(a) # (1, 2, 3, 4)
print(b) # (1, 2, 3)