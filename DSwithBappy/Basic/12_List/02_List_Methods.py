# Lists Methods/Functions
# Lists is Mutable, That means you can change the list

L = [1, 2, 3, 4]

# append
# will add at the end
print('append')
print(L.append(5)) # None
print(L) # [1, 2, 3, 4, 5]
L.append([6, 7, 8])
print(L) # [1, 2, 3, 4, 5, [6, 7, 8]]
L.append(True)
print(L) # [1, 2, 3, 4, 5, [6, 7, 8], True]

print()

# editing with indexing
L = [1, 2, 3, 4]
L[2] = 200
print('editing with indexing')
print(L) # [1, 2, 200, 4]

print()

# editing with slicing
L = [1, 2, 3, 4]
L[1:4] = [200, 300, 400]
print('editing with slicing')
print(L) # [1, 200, 300, 400]

print()

# extend
L = [1, 2, 3, 4]
a = [10, 11, 12]
print('extend')
print(L.extend(a)) # None
print(L) # [1, 2, 3, 4, 10, 11, 12]
L.extend('Python')
print(L) # [1, 2, 3, 4, 10, 11, 12, 'P', 'y', 't', 'h', 'o', 'n']

print()

# insert
L = [1, 2, 3, 4]
print('insert') 
print(L.insert(1, 200)) # None
print(L) # [1, 200, 2, 3, 4]

print()

# Deleting items from a list
L = [1, 2, 3, 4]
print('Deleting')
del L[0]
print(L) # [2, 3, 4]

L = [1, 2, 3, 4]
del L[1:3]
print(L) # [1, 4]

print()

# remove
L = [1, 2, 3, 4]
print('remove')
print(L.remove(3)) # None
print(L) # [1, 2, 4]

print()

# pop
L = [1, 2, 3, 4]
print('pop')
print(L.pop()) # 4
print(L) # [1, 2, 3]

print()

# clear
L = [1, 2, 3, 4]
print('clear')
print(L.clear()) # None
print(L) # []

print()

# len
L = [1, 2, 3, 4]
print('len')
print(len(L)) # 4 

print()

# min
L = [100, 2, 3, 4]
print('min')
print(min(L)) # 2

print()

# max
L = [100, 2, 3, 4]
print('max')
print(max(L)) # 100

print()

# sorted
L = [100, 2, 3, 4]
print('sorted')
print(sorted(L)) # [2, 3, 4, 100]
print(sorted(L, reverse=False)) # [2, 3, 4, 100]
print(sorted(L, reverse=True)) # [100, 4, 3, 2]

print()


# count
L = [1, 2, 3, 4, 4, 4, 5, 5]
print('count')
print(L.count(1)) # 1
print(L.count(2)) # 1
print(L.count(3)) # 1
print(L.count(4)) # 3
print(L.count(5)) # 2
print(L.count(6)) # 0

print()


# index
L = [1, 2, 3, 4, 4, 4, 5, 5]
print('index')
print(L.index(1)) # 0
print(L.index(2)) # 1
print(L.index(3)) # 2
print(L.index(4)) # 3
print(L.index(5)) # 6
# print(L.index(6)) # ValueError: 6 is not in list

print()

# reverse
L = [1, 2, 3, 4]
print('reverse')
print(L.reverse()) # None
print(L) # [4, 3, 2, 1]

print()

# sort
L = [4, 2, 1, 55, 10]
print('sort')
print(L.sort()) # None
print(L) # [1, 2, 4, 10, 55]

print()

# copy
L = [1, 2, 3, 4]
print('copy')
L1 = L.copy()
print(L) # [1, 2, 3, 4]
print(L1) # [1, 2, 3, 4]
L.append(500)
print(L) # [1, 2, 3, 4, 500]
print(L1) # [1, 2, 3, 4]

print()