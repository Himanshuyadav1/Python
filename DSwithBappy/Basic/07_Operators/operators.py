# 6 types of Operators in Python

# 1. Arithmetic Operators
# 2. Relational Operators
# 3. Logical Operators
# 4. Bitwise Operators
# 5. Assignment Operators
# 6. Membership Operators

# 1. Arithmetic Operators
# + - * / // % = **
print("Arithmetic Operators Results")
print(4+3)
print(4-3)
print(4*3)
print(12/5)
print(14//5) # integer division operator
print(4%2) # reminder operator
print(5**2) # power operator
print()

# 2. Relational Operators
# < > <= >= == !=
print("Relational Operators Results")
print(1<2) # True
print(1>2) # False
print(1<=2) # Ture
print(1>=2) # False
print(1==2) # False
print(1!=2) # Ture
print()

# 3. Logical Operators
# and or not
print("Logical Operators Results")
print(1 and 0) # 0
print(2 and 3) # 3
print(0 or 1) # 1
print(3 or 2) # 3
print(not 0) # True
print(not 1) # False
print(not 2) # False
print()

# 4. Bitwise Operators
# &(bitwise and) |(bitwise or) ^(bitwise xor) ~(bitwise not) >>(right shift) <<(left shift)
print("Bitwise Operators Results")
print(2 & 3)
print(2 | 3)
print(2 ^ 3)
print(~3)
print(4 >> 2)
print(5 << 2)
print()

# 5. Assignment Operators
# = += -= *= /= //= 
# ++ -- these are not supported by Python
print("Assignment Operators Results")
a = 2
print(a)
a += 1
print(a)
a -= 2
print(a)
a *= 5
print(a)
a /= 5
print(a)
b = 4
b //= 2
print(b)
print()

# 6. Membership Operators
# in not in
print("Membership Operators Results")
print('V' in 'Varanasi')
print('v' in 'Varanasi')
print('s' in 'Varanasi')
print('B' not in 'Varanasi')
print(1 in [1, 2, 3, 4])
print(10 not in [1, 2, 3, 4])