# Tuple Unpacking
print('Tuple Unpacking')

a, b, c = (1, 2, 3)

print(a, b, c) # 1 2 3

print()

# a, b = (1, 2, 3) # ValueError: too many values to unpack (expected 2)

a, b, *others = (1, 2, 3, 4)

print(a, b) # 1 2
print(others) # [3, 4]
print(type(others)) # <class 'list'>

print()

# zipping tuples
print('zipping tuples')
print('zipping tuples with same number of elements')
a = (1, 2, 3, 4)
b = (5, 6, 7, 8)

print(zip(a, b)) # <zip object at 0x00000235D673AC40> 
print(tuple(zip(a, b))) # ((1, 5), (2, 6), (3, 7), (4, 8))

print()

print('zipping tuples with different number of elements')
a = (1, 2, 3, 4)
b = (5, 6, 7)

print(zip(a, b)) # <zip object at 0x0000017E538CBD40>
print(tuple(zip(a, b))) # ((1, 5), (2, 6), (3, 7))

print()

# List Unpacking
print('List Unpacking')

a, b, c = [1, 2, 3]

print(a, b, c) # 1 2 3

# a, b = [1, 2, 3] # ValueError: too many values to unpack (expected 2)

a, b, *others = [1, 2, 3, 4, 5]
print(a, b) # 1 2
print(others) # [3, 4, 5]