# Find the sum of a 3 digit number entered by the user

num = int(input("Enter 3 digit number: "))
first_digit = num // 100
second_digit = (num % 100) // 10
third_digit = (num % 100) % 10
print(first_digit + second_digit + third_digit)

