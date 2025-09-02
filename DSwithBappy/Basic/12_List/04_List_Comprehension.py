"""
List Comprehansion
-------------------
List Comprehansion provides a concise way of creating lists.

newlist = [expression for item in iterable if condition == True]

Advantages of List Comprehansion
* More time-efficient and space-efficient than loops.
* Reuire fewer lines of code.
* Transforms iterative statement into a formula.
"""

# Add 1 to 10 numbers to a list
print('Add 1 to 10 numbers to a list')
print('Using loop')
L = []

for i in range(1, 11):
    L.append(i)

print(L) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print('Using List Comprehansion')
LC = [i for i in range(1, 11)]
print(LC) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print()


# scalar multiplication on a vector
print('scalar multiplication on a vector')
print('Using loop')
v = [2, 3, 4]
s = -3

L = []

for i in v:
    result = i * s
    L.append(result)

print(L) # [-6, -9, -12]

print('Using List Comprehansion')
LC = [i * s for i in v]

print(LC) # [-6, -9, -12]

print()

# Show Squares
print('Show Squares')

L = [1, 2, 3, 4]

LC = [i**2 for i in L]

print(LC) # [1, 4, 9, 16]

print()

# Print all numbers divisible by 5 in the range of 1 to 50
print('Print all numbers divisible by 5 in the range of 1 to 50')
print('Using Loop')

L = []

for i in range(1, 51):
    if i % 5 == 0:
        L.append(i)

print(L) # [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]

print('Using List Comprehansion')

LC = [i for i in range(1, 51) if i % 5 == 0]
print(LC) # [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]

print()

# Find languages which start with letter p
print('Find languages which start with letter p')

languages = ['java', 'python', 'php', 'c', 'javascript']
L = []
print(languages)

print('Using Loop')
for language in languages:
    if language.startswith('p'):
        L.append(language)

print(L) # ['python', 'php']

print("Using List Comprehansion")
LC = [language for language in languages if language.startswith('p')]

print(LC) # ['python', 'php']