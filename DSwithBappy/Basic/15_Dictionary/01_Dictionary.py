"""
Dictionary

Dictionary in Python is a collection of key values, used to store data values like a map, which, unlike other data types which hold only a single value as an element.

In some programming languages it is known as map or assosiative arrays.

dict = {'name': 'Goku', 'age': 22, 'gender': 'male'}

Characterstics:
* Mutable
* Indexing has no meaning
* keys can't be duplicated
* keys can't be mutable items 
"""

# Create Dictionary
print('Create Dictionary')

# Empty Dictionary
print('Empty Dictionary')
d = {}
print(d) # {}
print(type(d)) # <class 'dict'>

print()

# 1D Dictionary
print('1D Dictionary')
d = {'name': 'Goku', 'age': 22, 'gender': 'male'}
print(d) # {'name': 'Goku', 'age': 22, 'gender': 'male'}
print(type(d)) # <class 'dict'>

print()

# With Mixed Keys
print('With Mixed Keys')
d = {'name': 'Goku', 1: 5, (1, 2, 3): 6}
print(d) # {'name': 'Goku', 1: 5, (1, 2, 3): 6}
print(type(d)) # <class 'dict'>

print()

# 2D Dictionary
print('2D Dictionary')
d = {
    'name': 'Goku',
    'college_name': 'ABC',
    'gender': 'male',
    'semester': 5,
    'subjects': {'DSA': 80, 'Math': 90, 'English': 70}
}
print(d) # {'name': 'Goku', 'college_name': 'ABC', 'gender': 'male', 'semester': 5, 'subjects': {'DSA': 80, 'Math': 90, 'English': 70}}
print(type(d)) # <class 'dict'>

print()

# Using sequence and dict function
print('Using sequence and dict function')
d = dict([('name', 'Goku'), ('age', 32)])
print(d) # {'name': 'Goku', 'age': 32}
print(type(d)) # <class 'dict'>

print()

# Duplicate Keys
print('Duplicate Keys')
d = {'name': 'Goku', 'name': 'Gohan', 'age': 22, 'gender': 'male'}
print(d) # {'name': 'Gohan', 'age': 22, 'gender': 'male'}
print(type(d)) # <class 'dict'>

print()

# Mutable items as keys
print('Mutable items as keys')
# d = {'name': 'Goku', 1: 5, (1, 2, 3): 6, [1, 2, 3]: 7} # TypeError: unhashable type: 'list'
print("TypeError: unhashable type: 'list'")

print()

# Accessing Items
print('Accessing Items')

# 1D Dictionary
print('1D Dictionary')
d = {'name': 'Goku', 'age': 22, 'gender': 'male'}
print(d['name']) # Goku
print(d['age']) # 22
print(d['gender']) # male
# print(d['Gender']) # KeyError: 'Gender'

print()

# 2D Dictionary
print('2D Dictionary')
d = {
    'name': 'Goku',
    'college_name': 'ABC',
    'gender': 'male',
    'semester': 5,
    'subjects': {'DSA': 80, 'Math': 90, 'English': 70}
}
print(d['name']) # Goku
print(d['college_name']) # ABC
print(d['subjects']['Math']) # 90

print()

# Adding key-value pair
print('Adding key-value pair')
d = {'name': 'Goku', 'age': 22, 'gender': 'male'}
print(d) # {'name': 'Goku', 'age': 22, 'gender': 'male'}
d['height'] = 5.8
print(d) # {'name': 'Goku', 'age': 22, 'gender': 'male', 'height': 5.8}

print()

# Editing key-value pair
print('Editing key-value pair')
d = {'name': 'Goku', 'age': 22, 'gender': 'male'}
print(d) # {'name': 'Goku', 'age': 22, 'gender': 'male'}
d['name'] = 'Gohan'
d['height'] = 5.11
print(d) # {'name': 'Gohan', 'age': 22, 'gender': 'male', 'height': 5.11}

print()

# Remove key-value pair
print('Remove key-value pair')

# del
print('del')
d = {'name': 'Goku', 'age': 22, 'gender': 'male'}
del d['age']
print(d) # {'name': 'Goku', 'gender': 'male'}

print()

# pop
print('pop')
d = {'name': 'Goku', 'age': 22, 'gender': 'male'}
print(d.pop('age')) # 22
print(d) # {'name': 'Goku', 'gender': 'male'}

print()

# popitem
print('popitem')
d = {'name': 'Goku', 'age': 22, 'gender': 'male'}
print(d.popitem()) # ('gender', 'male')
print(d) # {'name': 'Goku', 'gender': 'male'}

print()

# clear
print('clear')
d = {'name': 'Goku', 'age': 22, 'gender': 'male'}
print(d.clear()) # None
print(d) # {}

print()