# Literals

# Binary Literals
a = 0b1010 # 0b denotes binary literals
print(a) # 1010 --> 10 in binary

# Octal Literals
b = 0o144 # 0o denotes octal literals
print(b) # 310 --> 200

# Decimal Literals
c = 200
print(c)

# Hexadecimal Literals
d = 0x12c # 0x denotes hexadecimal literals
print(d) # 12c --> 300

# Float Literals
float_1 = 1.5
float_2 = 1.5e2 # 1.5 * 10^2
float_3 = 1.5e-3 # 1.5 * 10^-3
print(float_1)
print(float_2)
print(float_3)

# Complex Literals
x = 3.14j
y = 1 + 2j
z = 3 - 4j

print(x.real, x.imag)
print(y.real, y.imag)
print(z.real, z.imag)

# String Literals
single_quote_string = 'This is Python'
double_quote_string = "This is Python"
multiline_string = """
This
    is
Python
"""
unicode_string = u"\U0001f600\U0001F606\U0001F923"
raw_string = r"raw \n string"
unraw_string = "raw \n string" #showing purpose only

print(single_quote_string)
print(double_quote_string)
print(multiline_string)
print(unicode_string)
print(raw_string)
print(unraw_string)

# Boolean Literals
# True = 1
# False = 0

a = True + 4
b = False + 10

print(a) # 5
print(b) # 10


# None Literal
a = None
print(a)

# x =  # will show error: SyntaxError: invalid syntax
x = None # For creating empty variable
print(x)