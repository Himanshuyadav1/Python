"""
Dictionary Comprehension

{ key: value for vars in iterable }
"""

# Print 1st 10 numbers and their squares
print('Print 1st 10 numbers and their squares')
# Using Loop
print('Using Loop')
d = {}

for i in range(11):
    d[i] = i**2

print(d) # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}

print()

print('Using Dictionary Comprehension')

dc = {i: i**2 for i in range(11)}
print(dc) # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}

print()

# Using if condition in dictionary comprehansive
print('Using if condition in dictionary comprehansive')

# Select the product from the products which have more than 0 qty
print('Select the product from the products which have more than 0 qty')

products = {'phone': 10, 'laptop': 0, 'charger': 32, 'tablet': 0}
print(products) # {'phone': 10, 'laptop': 0, 'charger': 32, 'tablet': 0}

selected_products = {}
# Using Loop
print('Using Loop')
print("1st way")

for product in products:
    if products[product] > 0:
        selected_products[product] = products[product]

print(selected_products) # {'phone': 10, 'charger': 32}

print()

print("2nd way")

selected_products = {}

for (key, value) in products.items():
    if value > 0:
        selected_products[key] = value

print(selected_products) # {'phone': 10, 'charger': 32}

print()

print('Using Dictionary Comprehension')
print('1st way')
dc = {product: products[product] for product in products if products[product] > 0}
print(dc) # {'phone': 10, 'charger': 32}

print()

print('2nd way')
dc = {key: value for (key, value) in products.items() if value > 0}
print(dc) # {'phone': 10, 'charger': 32}

print()

# Using zip
print('Using Zip')
print('Day wise temperature')

days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
temp_C = [30.5, 32.6, 31.8, 33.4, 29.8, 30.2, 29.9]

dc = {day: temp for (day, temp) in zip(days, temp_C)}
print(dc) # {'Sunday': 30.5, 'Monday': 32.6, 'Tuesday': 31.8, 'Wednesday': 33.4, 'Thursday': 29.8, 'Friday': 30.2, 'Saturday': 29.9}