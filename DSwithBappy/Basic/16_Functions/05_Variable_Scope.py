"""
Variable Scope in Functions

* Global Variables
* Local Variables
""" 

# Global Variable
print('Global Variable')
def g(y):
    print(x) # 5
    print(x+1) # 6
x = 5
g(x)
print(x) # 5

print()

# Local Variable
print('Local Variable')
def f(y):
    x = 1
    x += 1
    print(x) # 2    
x = 5
f(x)
print(x) # 5

print()

# Modifying Global Variable Without global Keyword
print('Modifying Global Variable Without global Keyword')
# You can't modify global variable normally

# def h(y):
#     x += 1 # UnboundLocalError: cannot access local variable 'x' where it is not associated with a value
# x = 5
# h(x)
# print(x)
print("UnboundLocalError: cannot access local variable 'x' where it is not associated with a value")

print()

# Modifying Global Variable With global Keyword
print('Modifying Global Variable With global Keyword')
#  You can modify global variable with global keyword but it is not recommended
def h(y):
    global x
    x += 1 
x = 5
h(x)
print(x) # 6

print()