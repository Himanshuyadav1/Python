"""
Frozenset

Frozen set is just an immutable version of s Python set object 
"""

# Frozenset
print('Frozenset')

fs1 = frozenset([1, 2, 3, 4])
fs2 = frozenset((3, 4, 5, 6))

print(fs1) # frozenset({1, 2, 3, 4})
print(type(fs1)) # <class 'frozenset'>

print(fs2) # frozenset({3, 4, 5, 6})
print(type(fs2)) # <class 'frozenset'>

print()

# Union (|)
print('Union (|)')
print(fs1 | fs2) # frozenset({1, 2, 3, 4, 5, 6})

print()

# Intersection (&)
print('Intersection (&)')
print(fs1 & fs2) # frozenset({3, 4})

print()

# Difference (-)
print('Difference (-)')
print(fs1 - fs2) # frozenset({1, 2})
print(fs2 - fs1) # frozenset({5, 6})

print()

# Symmetric Difference (^)
print('Symmetric Difference (^)')
print(fs1 ^ fs2) # frozenset({1, 2, 5, 6})

print()

# Membership
print('Membership')

print(2 in fs1) # True
print(5 not in fs1) # True
print(6 in fs1) # False
print(7 not in fs1) # True

print()

# Iteration
print('Iteration')

for i in fs1:
    print(i)
"""
1
2
3
4
"""

print()

# 2D
print('2D')
fs = frozenset([1, 2, frozenset([3, 4])])

print(fs) # frozenset({frozenset({3, 4}), 1, 2})
print(type(fs)) # <class 'frozenset'>

print()