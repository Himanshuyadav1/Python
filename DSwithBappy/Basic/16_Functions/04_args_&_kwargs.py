"""
*args and **kwargs

*args and **kwargs are special Python keywords that are used to pass the variable length of arguments to a function.

*args allows us to pass a variable number of non-keyword arguments to a function.

** kwargs allows us to pass any number of keyword arguments.

Keyword arguments mean that they contain a key-value pair, like a Python dictionary.

"""

def multiply(a, b, c, d):
    return a * b * c * d

print(multiply(2, 3, 4, 5)) # 120

print()

# *args
print('*args')

def multiply(*args):
    print(args) # (1, 2, 3, 3, 4, 4, 5)
    print(type(args)) # <class 'tuple'>
    product = 1
    for i in args:
        product = product * i
    
    return product


print(multiply(1, 2, 3, 3, 4, 4, 5)) # 1440

def multiply(*goku):
    print(goku) # (1, 2, 3, 3, 4, 4, 5)
    print(type(goku)) # <class 'tuple'>
    product = 1
    for i in goku:
        product = product * i
    
    return product


print(multiply(1, 2, 3, 3, 4, 4, 5)) # 1440

print()

# **kwargs
print('**kwargs')

def display(**kwargs):
    print(kwargs) # {'India': 'Delhi', 'Bangladesh': 'Dhaka', 'Srilanka': 'Colombo'}
    print(type(kwargs)) # <class 'dict'>

display(India="Delhi", Bangladesh="Dhaka", Srilanka="Colombo")

print()
def display(**goku):
    for (key, value) in goku.items():
        print(f"{key} -> {value}")

display(India="Delhi", Bangladesh="Dhaka", Srilanka="Colombo")

"""
India -> Delhi
Bangladesh -> Dhaka
Srilanka -> Colombo
"""