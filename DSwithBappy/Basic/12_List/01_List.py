"""
Lists

* What are Lists?
* Lists Vs Arrays
* Characterstics of a List
* How to create a List
* Access items from a List
* Editing items in a List
* Deleting items from a List
* Operations on Lists
* Functions on Lists
* List comprehension

What are Lists?
List is a data type where you can store multiple items under 1 name. More technically, lists act like dynamic arrays which means you can add more items on the fly.
L = [20, "Python", 4.5, [1, 3, 42]]

Lists Vs Arrays

Arrays in Java, C and C++
---------------------------
* Fixed size
* Homegeneous means same data type for all items of the array
* Speed of execution fast
* Less memory

List
------------
* Dynamic sinze
* Hetrogeneous means different data type for all items of the array
* Speed of execution slow
* More memory

Characterstics of a List
* Ordered
* Changeable/Mutable
* Hetrogeneous
* Can have duplicates
* are dynamic
* can be nested
* items can be accessed
* can contain any kind of objects in python
"""

# Creating a List
print("Creating a List")
# Empty
print([]) # []
# 1D
print([1,2,3,4,5]) # [1,2,3,4,5]
# 2D
print([1,2,3,[4,5]]) # [1,2,3,[4,5]]
# 3D
print([[[1,2],[3,4]],[[5,6],[7,8]]]) # [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
# Hetrogeneous
print([1, True, 5.6, 5+6j, 'Python']) # [1, True, 5.6, (5+6j), 'Python']
# Usingn Type conversion
print(list('Python')) # ['P', 'y', 't', 'h', 'o', 'n']

print()

# Accessing items from a List
# * indexing
# * slicing

L = [1, 2, 3, 4, 5]

# Indexing
print(L[0]) # 1
print(L[2]) # 3
print(L[4]) # 5
print(L[-1]) # 5
print(L[-2]) # 4


# Slicing
print(L[0:2]) # [1, 2]
print(L[2:]) # [3, 4, 5]
print(L[:]) # [1, 2, 3, 4, 5]
print(L[::2]) # [1, 3, 5]
