for i in range(1, 5):
    for j in range(1, 5):
        print(i, j)

# Exercise - print half triangle

row = int(input("Enter the number of rows: "))

# 1st approach
print("1st approach")
for i in range(1, row + 1):
    for j in range(1, row + 1):
        if i >= j:
            print("*", end="")
        elif j == row:
            print()

print()

# 2nd approach
print("2nd approach")
for i in range(1, row +1):
    for j in range(1, i+1):
        print("*", end="")
    print()