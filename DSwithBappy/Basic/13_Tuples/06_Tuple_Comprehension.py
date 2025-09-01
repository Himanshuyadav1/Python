"""
Tuple Comprehension

You might have read about list comprehension in Python. However, there is no tuple comprehension in Python. But we will discuss how we can emulate tuple comprehension in Python.
"""

# Add 1 to 10 numbers to a list
print('Add 1 to 10 numbers to a list')
print('Using loop')
L = []

for i in range(1, 11):
    L.append(i)

print(L) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print('Emulate Tuple Comprehansion')
TC = (i for i in range(1, 11))
print(TC) # <generator object <genexpr> at 0x0000019E39F365C0>

TC = tuple((i for i in range(1, 11)))
print(TC) # (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

print()


# scalar multiplication on a vector
print('scalar multiplication on a vector')
print('Using loop')
v = (2, 3, 4)
s = -3

T = ()

for i in v:
    result = i * s
    T = T + (result,)

print(T) # (-6, -9, -12)

print('Emulate Tuple Comprehansion')
T = (i * s for i in v)
TC = tuple((i * s for i in v))

print(T) # <generator object <genexpr> at 0x000001A63A3765C0>
print(TC) # (-6, -9, -12)

print()

# Show Squares
print('Show Squares')

T = (1, 2, 3, 4)

TC = tuple((i**2 for i in T))

print(TC) # (1, 4, 9, 16)

print()

# Print all numbers divisible by 5 in the range of 1 to 50
print('Print all numbers divisible by 5 in the range of 1 to 50')
print('Using Loop')

T = ()

for i in range(1, 51):
    if i % 5 == 0:
        T = T + (i,)

print(T) # (5, 10, 15, 20, 25, 30, 35, 40, 45, 50)

print('Emulate Tuple Comprehansion')

TC = tuple((i for i in range(1, 51) if i % 5 == 0))
print(TC) 

print()

# Find languages which start with letter p
print('Find languages which start with letter p')

languages = ('java', 'python', 'php', 'c', 'javascript')
T = ()
print(languages)

print('Using Loop')
for language in languages:
    if language.startswith('p'):
        T = T + (language,)

print(T) # ('python', 'php')

print("Using List Comprehansion")
TC = tuple((language for language in languages if language.startswith('p')))

print(TC) # ('python', 'php')