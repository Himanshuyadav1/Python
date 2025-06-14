# Implicit - Internally by Python
# Explicit - By the programmer

# Implicit
print(5 + 5.5)

print(type(5))
print(type(5.5))


# Explicit
# print(5 + "5") # will show error
print(5 + int("5"))
print(5 + float("5"))

num = 1+2j
print(type(num))

# int(num) # will show error: TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
# float(num) # will show error: TypeError: float() argument must be a string or a real number, not 'complex'