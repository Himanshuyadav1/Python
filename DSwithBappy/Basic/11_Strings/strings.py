"""
Strings are sequence of characters

In Python specifically, strings are a sequence of Unicode characters.
https://docs.python.org/3/howto/unicode.html

Topics:
    * Creation Strings
    * Accessing Strings
    * Adding Chars to Strings
    * Editing Strings
    * Deleting Strings
    * Operations on Strings
    * String Functions 
"""

# Creation Strings
print("Creation Strings")
s = 'hello'
print(s)
s = "hello"
print(s)
# Multiline strings
s = '''
Thank
you
'''
print(s)
s = """
Thank
you
"""
print(s)
s = str("hello")
print(s)

print()

# String length
print("Length of string")
s = "Welcome to Python"
print(len(s))
print()

# Accessing Strings
print("Accessing Strings")
s = "Welcome to Python"

# Positive indexing
print(s[5]) # m
# print(s[50]) # will show error IndexError: string index out of range

# Negative indexing
s = "Welcome to Python"
print(s[-5]) # y

# String slicing
s = "Welcome to Python"
# In positive first index should be less than second
print(s[0:7]) # Welcome
print(s[11:17]) # Python
print(s[0:]) # Welcome to Python
print(s[1:]) # elcome to Python
print(s[:5]) # Welcom
print(s[:]) # Welcome to Python
print(s[0:7:1]) # Welcome
print(s[0:7:2]) # Wloe
print(s[0:7:3]) # Wce
print(s[6:0:-1]) # emocle
print(s[7:0:-1]) #  emocle
print(s[6:0:-2]) # eol
print(s[7:0:-2]) #  mce
print(s[::-1]) # nohtyP ot emocleW
print(s[::-2]) # nhy teolW
print(s[-6:]) # Python
# In negative first index should be bigger than second
print(s[-1:-7:-1]) # nohtyP

print()

# Python strings are immutable
# Adding Chars to Strings
s = "Welcome to Python"
# s[0] = 'A' # show error TypeError: 'str' object does not support item assignment

# Editing Strings
# s[1] = 'A' # show error TypeError: 'str' object does not support item assignment

# Deleting Strings
# del s[0] # show error TypeError: 'str' object doesn't support item deletion

del s # this will delete the whole object.
