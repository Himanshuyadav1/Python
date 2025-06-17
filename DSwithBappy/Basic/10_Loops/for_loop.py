print("For loop with range")
for i in range(1, 11):
    print(i)

print()
# range with step
print("For loop with range-step 2")
for i in range(1, 11, 2):
    print(i)

print()

print("For loop with range-step 3")
for i in range(1, 11, 3):
    print(i)

print()

print("For loop print number in reverse order")
for i in range(10, 0, -1):
    print(i)

print()

print("For loop with string")
for i in "Python":
    print(i)

print()

print("For loop with list")
for i in [1, 2, 3, 4, 5]:
    print(i)

print()

print("For loop with tuple")
for i in (1, 2, 3, 4, 5):
    print(i)

"""
Program - The current population of a town is 10000. The Population of the town is increasing at the rate
of 10% per year. You have to write a program to find out the population at the end of each of the last
10 years.
"""

current_population = 10000
increasing_rate = 10

for i in range(10, 0, -1):
    print(i,"th year population: ", current_population)
    current_population = current_population - (current_population * increasing_rate)//100