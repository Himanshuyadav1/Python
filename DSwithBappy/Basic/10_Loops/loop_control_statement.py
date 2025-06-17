"""
Break
Continue
Pass
"""

print("Break statement")
for i in range(1, 11):
    if i == 5:
        break
    print(i)

print()

# Exercise for break
# print prime number upto 100
lower = int(input("Enter lower range: "))
upper = int(input("Enter upper range: "))

print("Prime numbers from", lower, "to", upper)
for i in range(lower, upper + 1):
    for j in range(2, i):
        if i%j == 0:
            break
    else:
        print(i)

# Continue
print("Continue statement")
for i in range(1, 6):
    if i == 3:
        continue
    print(i)

# Pass
print("Pass statement")
for i in range(1, 10):
    pass
print("The pass statement is used as a placeholder for future code.")