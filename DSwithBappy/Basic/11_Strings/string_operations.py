"""
Operations on Strings

    * Arithmetic Operations
    * Relational Operations
    * Logical Operations
    * Loops on Strings
    * Membership Operations
"""

# Arithmetic Operations
print("Arithmetic Operations")
# concatination
print("Hi" + " " + "Everyone")

print("Hi" * 5)
print("*" * 5)

print()

# Relational Operations
print("Relational Operations")
# equality
print("Hello" == "Hello") # True
# not equal
print("Hello" != "World") # True
# greater than
print("Hello" > "Hi") # False
print("A" > "B") # False
# less than
print("Hello" < "World") # True
# greater than or equal to
print("Hello" >= "Hello") # True

print()

# Logical Operations
print("Logical Operations")
print("Hello" and "World") # "World"
print("Hello" or "World") # "Hello"
print("" or "World") # "World"
print(" " or "World") # " "
print(not "Hello") # False
print(not "") # True
print(not " ") # False

print()

# Membership Operations
print("Membership Operations")
print("H" in "Hello") # True
print("w" in "Hello") # False
print("A" not in "Hello") # True
print("e" not in "Hello") # False

print()

# Loops on Strings
print("Loops on Strings")
for i in "Python":
    print(i)