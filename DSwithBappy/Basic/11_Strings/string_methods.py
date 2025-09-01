"""
Common Funtions/Method
    * len
    * max
    * min
    * sorted
"""

s = "Welcome to Python"

print("len Method")
print(len(s)) # 17

print()

print("max Method")
# on the basis of ascii value it return result
print(max(s)) # y

print()

print("min Method")
# on the basis of ascii value it return result
print(min(s)) # ' '

print()

# Ascending order
print("sorted Method")
print(sorted(s)) # [' ', ' ', 'P', 'W', 'c', 'e', 'e', 'h', 'l', 'm', 'n', 'o', 'o', 'o', 't', 't', 'y']

print()

# Descending order
print("sorted Method with reverse True")
print(sorted(s, reverse=True)) # ['y', 't', 't', 'o', 'o', 'o', 'n', 'm', 'l', 'h', 'e', 'e', 'c', 'W', 'P', ' ', ' ']

print()

"""
Strings Functions/Method
    * Capitalize
    * Title
    * Upper
    * Lower
    * Swapcase
    * Count
    * Find
    * Index
    * endswith
    * startswith
    * format
    * f-strings
    * isalnum
    * isalpha
    * isdigit
    * isidentifier
    * split
    * join
    * replace
    * strip
"""

s = "welCoMe to PyThOn"

print("capitalize Method")
print(s.capitalize()) # Welcome to python

print()

print("title Method")
print(s.title()) # Welcome To Python

print()

print("upper Method")
print(s.upper()) # WELCOME TO PYTHON

print()

print("lower Method")
print(s.lower()) # welcome to python

print()

print("swapcase Method")
print(s.swapcase()) # WELcOmE TO pYtHoN

print()

print("count Method")
print(s.count("o")) # 2

print()

print("find Method")
print(s.find("o")) # 4
print("find Method with non existing characters")
print(s.find("z")) # -1

print()

print("index Method")
print(s.index("o")) # 4
# print(s.index("z")) # will show error ValueError: substring not found

print()

print("endswith Method")
print(s.endswith("On")) # True
print(s.endswith("on")) # False

print()

print("startswith Method")
print(s.startswith("we")) # True
print(s.startswith("We")) # False

print()

name = "Himanshu"
language = "Python"

s = "My name is {}, and I am learning {} language"

print("format Method")
print(s.format(name, language)) # My name is Himanshu, and I am learning Python language

print("format Method with controlled order")
s = "My name is {1}, and I am learning {0} language"
print(s.format(language, name)) # My name is Himanshu, and I am learning Python language

print()

print("f-strings Method")
name = "Himanshu"
language = "Python"

s = f"My name is {name}, and I am learning {language} language"
print(s) # My name is Himanshu, and I am learning Python language

print()

s1 = "Python"
s2 = "Python123"
s3 = "Python123@"
s4 = "123"

print("isalnum Method")
print(s1.isalnum()) # True
print(s2.isalnum()) # True
print(s3.isalnum()) # False
print(s4.isalnum()) # True

print()

print("isalpha Method")
print(s1.isalpha()) # True
print(s2.isalpha()) # False
print(s3.isalpha()) # False
print(s4.isalpha()) # False

print()

print("isdigit Method")
print(s1.isdigit()) # False
print(s2.isdigit()) # False
print(s3.isdigit()) # False
print(s4.isdigit()) # Ture

print()

s1 = "1name"
s2 = "@name"
s3 = "$name"
s4 = "_name"
s5 = "name1"
s6 = "name@"
s7 = "name$"
s8 = "name_"

print("isidentifier Method")
print(s1.isidentifier()) # False
print(s2.isidentifier()) # False
print(s3.isidentifier()) # False
print(s4.isidentifier()) # Ture
print(s5.isidentifier()) # Ture
print(s6.isidentifier()) # False
print(s7.isidentifier()) # False
print(s8.isidentifier()) # Ture

print()

s1 = "welcome to python"
s2 = "welcome: to: python"

print("split Method")
print(s1.split()) # ['welcome', 'to', 'python']
print(s2.split()) # ['welcome:', 'to:', 'python']

print(s1.split(" ")) # ['welcome', 'to', 'python']
print(s2.split(":")) # ['welcome', ' to', ' python']

print(type(s1.split())) # <class 'list'>
print(type(s2.split())) # <class 'list'>

print()

words = ["Welcome", "to", "python"]

s1 = ""
s2 = " "
s3 = "-"
s4 = "_"

print("join Method")
s1 = s1.join(words)
print(s1) # Welcometopython
s2 = s2.join(words)
print(s2) # Welcome to python
s3 = s3.join(words)
print(s3) # Welcome-to-python
s4 = s4.join(words)
print(s4) # Welcome_to_python

print()

s = "Welcome to JavaScript"

print("replace Method")
print(s.replace("JavaScript", "Python")) # Welcome to Python

print()

s1 = "Welcome      to     Python"
s2 = "Welcome      to     Python         "

print("strip Method")
print(len(s1)) # 26
print(s1.strip()) # Welcome      to     Python
print(len(s1.strip())) # 26

print(len(s2)) # 35
print(s2.strip()) # Welcome      to     Python
print(len(s2.strip())) # 26
