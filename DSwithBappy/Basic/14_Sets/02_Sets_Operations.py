# Sets Operations
print('Sets Operations')

s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8}

print(s1)
print(s2)
print()

# Union (|)
print('Union (|)')
print(s1 | s2) # {1, 2, 3, 4, 5, 6, 7, 8}

print()

# Intersection (&)
print('Intersection (&)')
print(s1 & s2) # {4, 5}

print()

# Difference (-)
print('Difference (-)')
print(s1 - s2) # {1, 2, 3}
print(s2 - s1) # {8, 6, 7}

print()

# Symmetric Difference (^)
print('Symmetric Difference (^)')
print(s1 ^ s2) # {1, 2, 3, 6, 7, 8}

print()

# Membership
print('Membership')
s = {1, 2, 3, 4, 5}

print(5 in s) # True
print(4 not in s) # False
print(6 in s) # False
print(7 not in s) # True

print()

# Iteration
print('Iteration')
s = {1, 2, 30, 4, 5}

for i in s:
    print(i)
"""
1
2
4
5
30
"""