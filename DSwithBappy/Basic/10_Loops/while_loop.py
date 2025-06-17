# Python has two primitive loop commands:
# while loops
# for loops

# For visualize the code
# https://pythontutor.com/

# while loop

i = 1

while i < 6:
    print("Python")
    i += 1

# program to print multiplication table

number = int(input("Enter the number: "))
i = 1

while i <= 10:
    print(number, " x ", i, " = ", number * i)
    i += 1


# while loop with else
    
x = 1

while x < 5:
    print(x)
    x += 1

else:
    print("Program Executed!")