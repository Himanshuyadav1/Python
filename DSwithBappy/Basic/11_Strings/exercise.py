"""
1. Find the length of a given string without the len() function
2. Extract username from a given email.
    Ex: if the email is python@gmail.com then the username should be python
3. Write a program that can check whether a given string is palindrome or not
    Ex: abba, malayalam, mam
"""

# Exercise 1:

s = "Welcome to Python"
lenth = 0

for i in s:
    lenth += 1

print(len(s))
print(f"Length of the {s} is {lenth}")
print();

# Exercise 2:
email = input("Enter your email id: ")
pos = email.index('@')

# print("Username: ", email.split('@')[0])
print("Username: ", email[0:pos])
print()

# Exercise 3:
word = input("Enter any word to check whether it is palindrome or not: ")
lower_case_word = word.lower();

for i in range(0, len(word)//2):
    if lower_case_word[i] != lower_case_word[len(word) - i -1]:
        print(f"{word} is not a palindrome.")
        break
else:
    print(f"{word} is a palindrome.")


