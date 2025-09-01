# Tuples Methods/Functions

t = (10, 2, 3, 40)

# len
print('len')
print(len(t)) # 4

print()

# min
print('min')
print(min(t)) # 2

print()

# max
print('max')
print(max(t)) # 40

print()

# sum
print('sum')
print(sum(t)) # 55

print()

# sorted
print('sorted')
print(sorted(t)) # [2, 3, 10, 40]
print(type(sorted(t))) # <class 'list'>
print(sorted(t, reverse=False)) # [2, 3, 10, 40]
print(sorted(t, reverse=True)) # [40, 10, 3, 2]

print()

# count
print('count')

t = (1, 2, 3, 3, 4, 5, 5)

print(t.count(1)) # 1 
print(t.count(2)) # 1
print(t.count(3)) # 2
print(t.count(4)) # 1
print(t.count(5)) # 2
print(t.count(6)) # 0

print()

# index
print('index')

t = (1, 2, 3, 3, 4, 5, 5)

print(t.index(1)) # 0 
print(t.index(2)) # 1
print(t.index(3)) # 2
print(t.index(4)) # 4
print(t.index(5)) # 5
# print(t.index(6)) # ValueError: tuple.index(x): x not in tuple

print()