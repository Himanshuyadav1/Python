"""
Functions are 1st class citizens

It act like data types

https://en.wikipedia.org/wiki/First-class_citizen
"""
# 1st class citizens
print('1st class citizens')

# type and id
print('type and id')

def square(num):
    return num**2

print(type(square)) # <class 'function'>
print(id(square)) # 1994893759552

print()

# reassign
print('reassign')

x = square
print(type(x)) # <class 'function'>
print(id(x)) # 1994893759552
print(x(4)) # 14

print()

# deleting a function
print('deleting a function')

del square
# print(square) # NameError: name 'square' is not defined
print("NameError: name 'square' is not defined")

print()

# storing
print('storing')
def square(num):
    return num**2

L = [1, 2, 3, 4, 5, square]
print(L[-1](2)) # 4

print()

# Is function mutable or immutable?
print('Is function mutable or immutable?')

S = {square}
print(S) # {<function square at 0x0000021AC7FBC220>}

print("function is immutable.")

print()

# returning a function
print("returning a function")

def f():
    def g(a,b):
        return a+b
    return g

val = f()
print(val) # <function f.<locals>.g at 0x0000028B9A16C360>
sum = f()(2,3)
print(sum) # 5

print()

# function as argument
print("function as argument")

def func_a():
    print('Inside func_a')

def func_b(z):
    print('Inside func_b')
    return z()

print(func_b(func_a))
"""
Inside func_b
Inside func_a
None
"""