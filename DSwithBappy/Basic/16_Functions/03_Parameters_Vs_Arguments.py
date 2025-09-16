def odd_even(num): # Parameter
    """
    This function checks if a given number is odd or even.
    input: any valid number/integer
    output: "Odd Number" / "Even Number"
    Created Date: 04-09-25
    """
    if type(num) == int:
        if num % 2 != 0:
            return "Odd Number"
        else:
            return "Even Number"
    else:
        return "Wrong Input"

res = odd_even(4) # Argument
print(res) # Even Number

print()

"""
Types of Arguments
* Default Argument
* Positional Argument
* Keyword Argument
"""

# Types of Arguments
print('Types of Arguments')
print('Default Argument')

def power(a, b):
    return a**b

# power() # TypeError: power() missing 2 required positional arguments: 'a' and 'b'

def power(a=2, b=3):
    return a**b

print(power(3)) # 27

print()

# Keyword Argument
print('Keyword Argument')
# If you know the parameter name

print(power(b=2,a=3)) # 9