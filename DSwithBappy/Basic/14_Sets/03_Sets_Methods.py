# Sets Methods
print('Sets Methods')

s = {3, 1, 4, 5, 2, 6}

print()

# len
print('len')
print(len(s)) # 6

print()

# sum
print('sum')
print(sum(s)) # 21

print()

# min
print('min')
print(min(s)) # 1

print()

# max
print('max')
print(max(s)) # 6

print()

# sorted
print('sorted')
print(sorted(s)) # [1, 2, 3, 4, 5, 6]
print(type(sorted(s))) # <class 'list'>
print(sorted(s, reverse=False)) # [1, 2, 3, 4, 5, 6]
print(sorted(s, reverse=True)) # [6, 5, 4, 3, 2, 1]

print()

# union
print('union')
s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8}
print(s1) # {1, 2, 3, 4, 5}
print(s2) # {4, 5, 6, 7, 8}

print(s1 | s2) # {1, 2, 3, 4, 5, 6, 7, 8}
print(s1.union(s2)) # {1, 2, 3, 4, 5, 6, 7, 8}
print(s2.union(s1)) # {1, 2, 3, 4, 5, 6, 7, 8}
print(s1) # {1, 2, 3, 4, 5}
print(s2) # {4, 5, 6, 7, 8}

print()

# update
print('update')
s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8}
print(s1) # {1, 2, 3, 4, 5}
print(s2) # {4, 5, 6, 7, 8}

print(s1.update(s2)) # None
print(s1) # {1, 2, 3, 4, 5, 6, 7, 8}
print(s2) # {4, 5, 6, 7, 8}

print()

# intersection
print('intersection')
s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8}
print(s1) # {1, 2, 3, 4, 5}
print(s2) # {4, 5, 6, 7, 8}

print(s1 & s2) # {4, 5}
print(s1.intersection(s2)) # {4, 5}
print(s2.intersection(s1)) # {4, 5}
print(s1) # {1, 2, 3, 4, 5}
print(s2) # {4, 5, 6, 7, 8}

print()

# intersection_update
print('intersection_update')
s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8}
print(s1) # {1, 2, 3, 4, 5}
print(s2) # {4, 5, 6, 7, 8}

print(s1.intersection_update(s2)) # None
print(s1) # {4, 5}
print(s2) # {4, 5, 6, 7, 8}

print()

# difference
print('difference')
s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8}
print(s1) # {1, 2, 3, 4, 5}
print(s2) # {4, 5, 6, 7, 8}

print(s1 - s2) # {1, 2, 3}
print(s1.difference(s2)) # {1, 2, 3}
print(s2 - s1) # {8, 6, 7}
print(s2.difference(s1)) # {8, 6, 7}
print(s1) # {1, 2, 3, 4, 5}
print(s2) # {4, 5, 6, 7, 8}

print()

# difference_update
print('difference_update')
s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8}
print(s1) # {1, 2, 3, 4, 5}
print(s2) # {4, 5, 6, 7, 8}

print(s1.difference_update(s2)) # None
print(s1) # {1, 2, 3}
print(s2) # {4, 5, 6, 7, 8}

print()

# symmetric_difference
print('symmetric_difference')
s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8}
print(s1) # {1, 2, 3, 4, 5}
print(s2) # {4, 5, 6, 7, 8}

print(s1 ^ s2) # {1, 2, 3, 6, 7, 8}
print(s1.symmetric_difference(s2)) # {1, 2, 3, 6, 7, 8}
print(s2 ^ s1) # {1, 2, 3, 6, 7, 8}
print(s2.symmetric_difference(s1)) # {1, 2, 3, 6, 7, 8}
print(s1) # {1, 2, 3, 4, 5}
print(s2) # {4, 5, 6, 7, 8}

print()

# symmetric_difference_update
print('symmetric_difference_update')
s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8}
print(s1) # {1, 2, 3, 4, 5}
print(s2) # {4, 5, 6, 7, 8}

print(s1.symmetric_difference_update(s2)) # None
print(s1) # {1, 2, 3, 6, 7, 8}
print(s2) # {4, 5, 6, 7, 8}

print()

# isdisjoint
print('isdisjoint')
s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8}
s3 = {1, 2, 3, 4}
s4 = {7, 8, 5, 6}

print(s1.isdisjoint(s2)) # False
print(s3.isdisjoint(s4)) # True

print()

# issubset
print('issubset')
s1 = {1, 2, 3, 4, 5}
s2 = {1, 2, 3}

print(s1.issubset(s2)) # False
print(s2.issubset(s1)) # True

print()

# issuperset
print('issuperset')
s1 = {1, 2, 3, 4, 5}
s2 = {3, 4, 5}

print(s1.issuperset(s2)) # True
print(s2.issuperset(s1)) # False

print()

# copy
print('copy')
s1 = {1, 2, 3}
s2 = {4, 5, 6, (7, 8, 9)}

s3 = s1.copy()
s4 = s2.copy()

print(s3) # {1, 2, 3}
print(s4) # {(7, 8, 9), 4, 5, 6}