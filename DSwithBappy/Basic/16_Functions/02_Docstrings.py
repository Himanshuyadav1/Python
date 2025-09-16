# Docstring
print('Docstring')

def odd_even(num):
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

res = odd_even("Goku")
print(res) # Wrong Input

print()


res = odd_even(4)
print(res) # Even Number

print()

# __doc__
print('__doc__')
print(odd_even.__doc__)
"""
This function checks if a given number is odd or even.
input: any valid number/integer
output: "Odd Number" / "Even Number"
Created Date: 04-09-25
"""

print()

print(max.__doc__)
"""
max(iterable, *[, default=obj, key=func]) -> value
max(arg1, arg2, *args, *[, key=func]) -> value

With a single iterable argument, return its biggest item. The
default keyword-only argument specifies an object to return if
the provided iterable is empty.
With two or more positional arguments, return the largest argument.
"""