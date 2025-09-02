# Sets Comprehension
print('Sets Comprehansion')

# Add 1 to 10 numbers to a list
print('Add 1 to 10 numbers to a list')
print('Using loop')
S = set()

for i in range(1, 11):
    S.add(i)

print(S) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

print('Using Set Comprehansion')
SC = {i for i in range(1, 11)}
print(SC) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

print()


# scalar multiplication on a vector
print('scalar multiplication on a vector')
print('Using loop')
v = {2, 3, 4}
s = -3

S = set()

for i in v:
    result = i * s
    S.add(result)

print(S) # {-6, -12, -9}

print('Using Set Comprehansion')
SC = {i * s for i in v}

print(SC) # {-6, -12, -9}

print()

# Show Squares
print('Show Squares')

S = {1, 2, 3, 4}

SC = {i**2 for i in S}

print(SC) # {16, 1, 4, 9}

print()

# Print all numbers divisible by 5 in the range of 1 to 50
print('Print all numbers divisible by 5 in the range of 1 to 50')
print('Using Loop')

S = set()

for i in range(1, 51):
    if i % 5 == 0:
        S.add(i)

print(S) # {35, 5, 40, 10, 45, 15, 50, 20, 25, 30}

print('Using Set Comprehansion')

SC = {i for i in range(1, 51) if i % 5 == 0}
print(SC) # {35, 5, 40, 10, 45, 15, 50, 20, 25, 30}

print()

# Find languages which start with letter p
print('Find languages which start with letter p')

languages = {'java', 'python', 'php', 'c', 'javascript'}
S = set()
print(languages)

print('Using Loop')
for language in languages:
    if language.startswith('p'):
        S.add(language)

print(S) # {'python', 'php'}

print("Using Set Comprehansion")
SC = {language for language in languages if language.startswith('p')}

print(SC) # {'python', 'php'}