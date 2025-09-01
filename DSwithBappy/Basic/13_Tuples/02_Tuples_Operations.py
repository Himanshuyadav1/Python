"""
Operations on Lists
* Arthmetic
* Membership 
* Loop
"""

# Arthmetic (+, *)
print('Arthmetic')
t1 = (1, 2, 3, 4)
t2 = (6, 7, 8, 9)

# concatination
print('concatination')
print(t1 + t2) # (1, 2, 3, 4, 6, 7, 8, 9)
print()
print('multiplication')
print(t1 * 2) # (1, 2, 3, 4, 1, 2, 3, 4)
print(t2 * 3) # (6, 7, 8, 9, 6, 7, 8, 9, 6, 7, 8, 9)
print(t1 * -1) # ()
print(t1 * -2) # ()
print(t1 * -3) # ()
# print(t1 * t2) # TypeError: can't multiply sequence by non-int of type 'tuple'

print()

# Membership
print('Membership')
t = (1, 2, 3, 4)

print(1 in t) # True
print(1 not in t) # False
print(5 in t) # False
print(5 not in t) # True

print()

# Loop
print('Loop')
t = (1, 2, 3, 4)

for i in t:
    print(i)
"""
1
2
3
4
"""