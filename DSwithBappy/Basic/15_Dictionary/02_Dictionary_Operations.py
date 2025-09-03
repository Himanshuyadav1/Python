"""
Dictionary Operations
* Membership
* Iteration
"""

# Dictionary Operations
print('Dictionary Operations')
d = {'name': 'Goku', 'age': 22, 'gender': 'male'}

# Membership
print('Membership')
print('name' in d) # True
print('height' not in d) # True
print('Goku' in d) # False
print('Goku' not in d) # True

print()

# Iteration
print('Iteration')

for i in d:
    print(i, d[i])
"""
name Goku
age 22
gender male
"""