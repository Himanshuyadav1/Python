"""
Exercise - 1
Find the min of 3 given numbers
"""

num_1 = int(input("Enter your first integer number: "))
num_2 = int(input("Enter your second integer number: "))
num_3 = int(input("Enter your third integer number: "))

if num_1 < num_2 and num_1 < num_3:
    print("Minimum number of the given numbers is: ", num_1)
elif num_2 < num_1 and num_2 < num_3:
    print("Minimum number of the given numbers is: ", num_2)
else:
    print("Minimum number of the given numbers is: ", num_3)