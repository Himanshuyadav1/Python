"""
Sets 
A set is an unordered collection of items. Every set element is unique (no duplicates) and must be immutable (cannot be changed).
However, a set itself is mutable. We can add or remove items from it.

Sets can also be used to perform mathematical set operations like union, intersection, symmetric difference, etc.

Characterstics:
* Unordered
* Mutable
* No Duplicates
* Can't contain mutable data types
"""

# Creating Sets
print('Creating Sets')
# Empty
print('Empty')
s = set()
print(s) # set()
print(type(s)) # <class 'set'>

s1 = {}
print(s1) # {}
print(type(s1)) # <class 'dict'>

print()

# 1D
print('1D')
s1 = {1, 2, 3}

print(s1) # {1, 2, 3}
print(type(s1)) # <class 'set'>

print()

# 2D
print('2D')
# s2 = {1, 2, 3, {4, 5}} # TypeError: unhashable type: 'set'
s2 = {1, 2, 3, (4, 5)}
print(s2) # {3, 1, (4, 5), 2}
print(type(s2)) # <class 'set'>

print()

# Homo
print('Homo')
s3 = {1, 2, 3}

print(s3) # {1, 2, 3}
print(type(s3)) # <class 'set'>

print()

# Hetro
print('Hetro')
s4 = {1, 'Python', 2, 2.5, (1, 2, 3)}

print(s4) # {1, 2, 2.5, 'Python', (1, 2, 3)} # ramdom position
print(type(s4)) # <class 'set'>

print()

# Type Conversion
print('Type Conversion')
s5 = set([1, 2, 3])
s6 = set((4, 5, 6))

print(s5) # {1, 2, 3}
print(type(s5)) # <class 'set'>
print(s6) # {4, 5, 6}
print(type(s6)) # <class 'set'>

print()

# Duplicates not allowed
print('Duplicates not allowed')
s7 = {1, 1, 2, 2, 3, 3}

print(s7) # {1, 2, 3}
print(type(s7)) # <class 'set'>

print()

# Set can't have mutable items
print("Set can't have mutable items")
# s8 = {1, 2, [3, 4]} # TypeError: unhashable type: 'list'
print("TypeError: unhashable type: 'list'")

print()

# Unordered
print('Unordered')
s8 = {1, 2, 3}
s9 = {3, 2, 1}

print(s8 == s9) # Ture

s8 = {1, 2, 31}
s9 = {3, 2, 1}

print(s8 == s9) # False

print()

# Accessing Items
print('Accessing Items')
print('Indexing')
s = {1, 2, 3}

# s[0] # TypeError: 'set' object is not subscriptable
print("TypeError: 'set' object is not subscriptable")

print()

print('Slicing')
# s[0:2] # TypeError: 'set' object is not subscriptable
print("TypeError: 'set' object is not subscriptable")

print()

# Editing Items
print('Editing Items')
s = {1, 2, 3}

# s[0] = 100 # TypeError: 'set' object does not support item assignment
print("TypeError: 'set' object does not support item assignment")

print()

# Adding Items
print('Adding Items')
S = {1, 2, 3, 4}

print(S.add(5)) # None # only add single item to the set
print(S) # {1, 2, 3, 4, 5}

print()

# Update Set
print('Update Set')
S = {1, 2, 3, 4}

print(S.update([5, 6, 7])) # None # add multiple items, which are list, to the set
print(S) # {1, 2, 3, 4, 5, 6, 7}

print()

# Deleting Items
print('Deleting Items')
S = {1, 2, 3, 4}

# del S[0] # TypeError: 'set' object doesn't support item deletion 
print("TypeError: 'set' object doesn't support item deletion")

print()

# discard
print('discard')
S = {1, 2, 3, 4, 5}
print(S.discard(5)) # None
print(S) # {1, 2, 3, 4}
print(S.discard(100)) # None
print(S) # {1, 2, 3, 4}

print()

# remove
print('remove')
S = {1, 2, 3, 4, 5}
print(S.remove(5)) # None
print(S) # {1, 2, 3, 4}
# print(S.remove(100)) # KeyError: 100

print()

# pop
print('pop')
S = {123, 242, 3, 4, 5}
print(S.pop()) # 242 # it picks randomly any item of set for deletion and return it.
print(S) # {3, 4, 5, 123}

print()

# clear
print('clear')
S = {1, 2, 3, 4, 5}

print(S.clear()) # None
print(S) # set()