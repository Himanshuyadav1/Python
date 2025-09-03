# Dictionary Methods/Functions
print('Dictionary Methods/Functions')

# Common Functions
print('Common Functions')
d = {'name': 'Goku', 'age': 22, 'gender': 'male'}
print(d) # {'name': 'Goku', 'age': 22, 'gender': 'male'}

# len
print('len')
print(len(d)) # 3

print()

# min
print('min')
print(min(d)) # age

print()

# max
print('max')
print(max(d)) # name

print()

# sorted
print('sorted')
print(sorted(d)) # ['age', 'gender', 'name']
print(type(sorted(d))) # <class 'list'>
print(sorted(d, reverse=False)) # ['age', 'gender', 'name']
print(sorted(d, reverse=True)) # ['name', 'gender', 'age']

print()

# Dictionary Methods/Functions
print('Dictionary Methods/Functions')
d = {'name': 'Goku', 'age': 22, 'gender': 'male'}
print(d) # {'name': 'Goku', 'age': 22, 'gender': 'male'}

print()

# items
print('items')
print(d.items()) # dict_items([('name', 'Goku'), ('age', 22), ('gender', 'male')])
print(type(d.items())) # <class 'dict_items'>

print()

# keys
print('keys')
print(d.keys()) # dict_keys(['name', 'age', 'gender'])
print(type(d.keys())) # <class 'dict_keys'>

print()

# values
print('values')
print(d.values()) # dict_values(['name', 'age', 'gender'])
print(type(d.values())) # <class 'dict_values'>

print()

# update
print('update')
d1 = {1: 2, 3: 4, 4: 5}
d2 = {4: 7, 6: 8}
print(d1.update(d2)) # None
print(d1) # {1: 2, 3: 4, 4: 7, 6: 8}
print(d2) # {4: 7, 6: 8}

print()

d1 = {1: 2, 3: 4, 4: 5}
d2 = {4: 7, 6: 8}
print(d2.update(d1)) # None
print(d1) # {1: 2, 3: 4, 4: 5}
print(d2) # {4: 5, 6: 8, 1: 2, 3: 4}