"""
Tuples
A tuple in Python is similar to a list. The difference between the two is that we cannot change the elements of a tuple once it is assgined whereas we can change the elements of a list.

In short, a tuple is an immutable list. A tuple can not be changed in any way once it is created.

Characterstics
* Ordered
* Unchangeble
* Allows duplicate

Topic to be discussed
* Creating a Tuple
* Accessing items
* Editing items
* Adding items
* Deleting items
* Operations on Tuples
* Tuple Functions
"""

# Creating Tuples
print('Creating Tuples')
print()
# Empty tuple
print('Empty tuple')
t1 = ()
print(t1) # ()
print(type(t1)) # <class 'tuple'>

print()

# Create a tuple with a single item
print('Create a tuple with a single item')
t2 = ("Python") 
print(t2) # Python
print(type(t2)) # <class 'str'>

t3 = ("Python",) # In case of single item , must be added
print(t3) # ('Python',)
print(type(t3)) # <class 'tuple'>

print()

# homo tuple
print('homo tuple')
t4 = (1, 2, 3, 4)
print(t4) # (1, 2, 3, 4)
print(type(t4)) # <class 'tuple'>

print()

# hetro tuple
print('hetro tuple')
t5 = (1, 2.5, True, [1, 2, 3, 4])
print(t5) # (1, 2.5, True, [1, 2, 3, 4])
print(type(t5)) # <class 'tuple'>

print()

# nested tuple
print('nested tuple')
t6 = (1, 2, 3, (4, 5))
print(t6) # (1, 2, 3, (4, 5))
print(type(t6)) # <class 'tuple'>

print()

# using type conversion
print('using type conversion')
t7 = tuple('Python')
print(t7) # ('P', 'y', 't', 'h', 'o', 'n')
print(type(t7)) # <class 'tuple'>

print()

# Accessing Items
# * Indexing
# * Slicing

print('Accessing Items')
print('Indexing')
t = (1, 2, 3, 4)

print(t[0]) # 1
print(t[1]) # 2
print(t[-1]) # 4
print(t[-2]) # 3
# print(t[20]) # IndexError: tuple index out of range

print()

print('Slicing')
print(t[0:3]) # (1, 2, 3)
print(t[::2]) # (1, 3)

print()

# Editing items / Deleting items
t = (1, 2, 3, 4)
# t[0] = 100 # TypeError: 'tuple' object does not support item assignment
# del t[0] # TypeError: 'tuple' object doesn't support item deletion

# Type Casting
print('Editing using type casting')
temp = list(t)
print(temp) # [1, 2, 3, 4]

temp.append(200)
print(temp) # [1, 2, 3, 4, 200]

t = tuple(temp)
print(t) # (1, 2, 3, 4, 200)