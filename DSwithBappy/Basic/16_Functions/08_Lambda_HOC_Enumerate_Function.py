"""
Lambda Function

A lambda function is a small anonymous function.

A lambda function can take any number of arguments, but can only have one expression.

lambda a,b: a+b

Diff between lambda vs normal function
* No name
* lambda has no return value(infact, returns a function)
* lambda is written in 1 line
* not reusable

Then why use lambda functions?
They are used with HOF
"""


# Square
print('Square')

a = lambda x: x**2
print(a) # <function <lambda> at 0x000001F0B82A1440>
print(a(4)) # 16

print()

# Add
print('Add')

b = lambda x, y: x + y
print(b) # <function <lambda> at 0x000002B3E5BCC040>
print(b(4, 2)) # 6

print()

# Check if a string has 'a'
print("Check if a string has 'a'")

a = lambda s: 'a' in s
print(a('Hello')) # False
print(a('Tea')) # True

print()

# odd or even
print('odd or even')

a = lambda num: 'even' if num % 2 == 0 else 'odd'
print(a(3)) # odd 
print(a(4)) # even

print()

# Higher Order Functions
print('Higher Order Functions')

L = [1, 2, 3, 4, 5]

def Square(x):
    return x**2

def Cube(x):
    return x**3

# Higher Order Function (HOF)
def Transform(f, L):
    output = []
    for i in L:
        output.append(f(i))
    return output

print(Transform(Square, L)) # [1, 4, 9, 16, 25]
print(Transform(Cube, L)) # [1, 8, 27, 64, 125]

# Using Lambda Function
print("Using Lambda Function")
print(Transform(lambda x: x**2, L)) # [1, 4, 9, 16, 25]
print(Transform(lambda x: x**3, L)) # [1, 8, 27, 64, 125]

print()

"""
Higher Order functions

- map
- filter
- reduce 
"""

# map
print("map")

# Square the items of a list
print('Square the items of a list')
L = [1, 2, 3, 4, 5]

result = map(lambda x: x**2, L)
print(result) # <map object at 0x0000024008B30CD0>
print(list(result)) # [1, 4, 9, 16, 25]
print(L) # [1, 2, 3, 4, 5]

print(list(map(lambda x: x**2, [1, 2, 3, 4, 5]))) # [1, 4, 9, 16, 25]

print()

# odd/even labelling of a list items
print("odd/even labelling of a list items")
L = [1, 2, 3, 4, 5]

result = map(lambda x: 'odd' if x % 2 != 0 else 'even', L)
print(result) # <map object at 0x0000018C2CC716F0>
print(list(result)) # ['odd', 'even', 'odd', 'even', 'odd']
print(L) # [1, 2, 3, 4, 5]

print(list(map(lambda x: 'odd' if x % 2 != 0 else 'even', [1, 2, 3, 4, 5]))) # ['odd', 'even', 'odd', 'even', 'odd']

print()

# fetch names from a list of dict
print("fetch names from a list of dict")

users = [
    {
        'name': 'Goku',
        'age': 30,
        'gender': 'male'
    },
    {
        'name': 'Gohan',
        'age': 23,
        'gender': 'male'
    },
    {
        'name': 'Gotan',
        'age': 33,
        'gender': 'male'
    }
]

result = map(lambda user: user['name'], users)
print(result) # <map object at 0x00000272515D1D50>
print(list(result)) # ['Goku', 'Gohan', 'Gotan']

print(list(map(lambda user: user['name'], users))) # ['Goku', 'Gohan', 'Gotan']

print()

# filter
print('filter')

# numbers greater than 2
print('numbers greater than 2')
L = [1, 2, 3, 4, 5]

result = filter(lambda num: num > 2, L)
print(result) # <filter object at 0x0000019DADC223B0>
print(list(result)) # [3, 4, 5]
print(L) # [1, 2, 3, 4, 5]

print(list(filter(lambda num: num > 2, L))) # [3, 4, 5]

print()


# fetch fruits starting with "a"
print('fetch fruits starting with "a"')

fruits = ['apple', 'guava', 'cherry']

result = filter(lambda fruit: fruit.startswith('a') , fruits)
print(result) # <filter object at 0x00000210CE1829B0>
print(list(result)) # ['apple']
print(fruits) # ['apple', 'guava', 'cherry']

print(list(filter(lambda fruit: fruit.startswith('a'), fruits))) # ['apple']

print()

# reduce
print('reduce')

# sum of all item
print('sum of all item')

import functools

L = [1, 2, 3, 4, 5]

result = functools.reduce(lambda num1, num2: num1 + num2, L)
print(result) # 15 
print(L) # [1, 2, 3, 4, 5]

print(functools.reduce(lambda num1, num2: num1 + num2, L)) # 15

print()

# find min
print('find min')

import functools

L = [23, 11, 45, 10, 5]

result = functools.reduce(lambda num1, num2: num1 if num1 < num2 else num2, L)
print(result) # 5 
print(L) # [23, 11, 45, 10, 5]

print(functools.reduce(lambda num1, num2: num1 if num1 < num2 else num2, L)) # 5

print()

# Enumerate Function in Python
print('Enumerate Function in Python')

names = ['Goku', 'Chichi', 'Gohan', 'Gotan']

print(enumerate(names)) # <enumerate object at 0x000001A45612BF10>

for obj in enumerate(names):
    print(obj)

"""
(0, 'Goku')
(1, 'Chichi')
(2, 'Gohan')
(3, 'Gotan')
"""
print()

for index, name in enumerate(names):
    print(index, name)

"""
0 Goku
1 Chichi
2 Gohan
3 Gotan
"""

print()

for index, name in enumerate(names, start=1):
    print(index, name)

"""
1 Goku
2 Chichi
3 Gohan
4 Gotan
"""

print()

for index, name in enumerate(names, start=1):
    if index == 3:
        print(name) # Gohan