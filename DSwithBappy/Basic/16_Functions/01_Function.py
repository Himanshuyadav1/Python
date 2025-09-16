"""
What are Functions?

Functions is a Programming construct. It takes input & returns outputs.

There are 2 types of functions:
1. Builtin
2. User Define

Benefit of Functions is Code Reusability.

Principle of functions:
1. Abstraction: There is something exist but you can't see that.
2. Decomposition: Combining small functions to build product/project.

def add(num1, num2) {
    addition = num1 + num2
    return addition
}

result = add(2, 4)
print(result)

Note: 
1. num1 and num2 are parameters
2. 2 and 4 are arguments

Benefits of using a Function
* Code Modularity
* Code Readibility
* Code Reusability
"""

# Creating Functions
print('Creating Functions')

def greet():
    output = "Hello All! Welcome to Python World"
    return output

result = greet()
print(result) # Hello All! Welcome to Python World

print()

def greet(name):
    output = f"Hello {name}! Welcome to DBZ World"
    return output

names = ["Goku", "Gohan", "vegeta"]

for name in names:
    result = greet(name)
    print(result)

"""
Hello Goku! Welcome to DBZ World
Hello Gohan! Welcome to DBZ World
Hello vegeta! Welcome to DBZ World
"""