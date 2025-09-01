# 1. Show no of items available
print('1. Show no of items available')
car_name = ["Audi", "BMW", "TATA", "Volvo"]
no_of_cars = [10, 20, 30, 5]

print('Using loop')
for i, j in zip(car_name, no_of_cars):
    print(f"{i} = {j}")
"""
Audi = 10
BMW = 20
TATA = 30
Volvo = 5
"""
print('Using List Comprehansion')
LC = [f"{i} = {j}" for i, j in zip(car_name, no_of_cars)]
print(LC) # ['Audi = 10', 'BMW = 20', 'TATA = 30', 'Volvo = 5']

print()

"""
2. You are given a list of integers. You are asked to make a list by running through elements of the list by adding all elements greater and itself. 
"""
print('2. You are given a list of integers. You are asked to make a list by running through elements of the list by adding all elements greater and itself.')
L = [2, 4, 6, 10, 1]
result = []

for i in L:
    sum = 0
    for j in L:
        if i <= j:
            sum = sum + j
    result.append(sum)

print(result) # [22, 20, 16, 10, 23]

print()

# 3. Find list of common unique items from two list and show in increasing order
print('3. Find list of common unique items from two list and show in increasing order')
num1 = [23, 45, 67, 78, 89, 34, 67]
num2 = [34, 89, 55, 56, 39, 67, 67]

result = []

print('Approach 1')
for i in num1:
    for j in num2:
        if i == j and i not in result:
            result.append(i)

result.sort()
print(result)

print('Approach 2')
for i in num1:
    if i in num2:
        if i not in result:
            result.append(i)

result.sort()
print(result)
