"""
Operations on Lists
* Arthmetic
* Membership 
* Loop
"""

# Arthmetic (+, *)
print('Arthmetic')
L1 = [1, 2, 3, 4, 5]
L2 = [5, 6, 7, 8, 9]

# concatination
print(L1 + L2) # [1, 2, 3, 4, 5, 5, 6, 7, 8, 9]

print(L1 * 2) # [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
print(L1 * 3) # [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
# print(L1 * L2) # TypeError: can't multiply sequence by non-int of type 'list'

print()

# Membership
print('Membership')
L1 = [1, 2, 3, 4, 5]
L2 = [5, 6, [7, 8, 9]]

print(3 in L1) # True
print(4 in L1) # True
print(30 in L1) # False
print(30 not in L1) # True
print(6 in L2) # True
print(8 not in L2) # True
print([7, 8, 9] in L2) # True
print([7, 8, 90] not in L2) # True

print()


# Loop
print('Loop')
L1 = [1, 2, 3, 4, 5]
L2 = [5, 6, [7, 8, 9]]

for i in L1:
    print(i)
"""
1
2
3
4
5
"""

for i in L2:
    print(i)
"""
5
6
[7, 8, 9]
"""

