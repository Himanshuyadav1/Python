# Nested Conditions
# Login Function demo - Dragonweb

"""
Assume Credentials
Email: drangon7@example.com
Password: 12345
"""

email = input("Enter your email: ")
password = input("Enter your password: ")

if email == "drangon7@example.com" and password == "12345":
    print("Login Successfully!!")
elif email == "drangon7@example.com" and password != "12345":
    print("Please try again!")
    password = input("Enter your correct password: ")
    if password == "12345":
        print("Success!")
    else:
        print("Wrong!")
else:
    print("Invalid Credentials!")