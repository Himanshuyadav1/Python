import random

random_number = random.randint(1, 100)
user_number = int(input("Guess the Number: "))

counter = 1

while random_number != user_number:
    if(user_number > random_number):
        print("You provided higher number. Please try again")
    else:
        print("You provided lower number. Please try again")
    user_number = int(input("Guess the Number: "))
    counter += 1

else:
    print("Congratulation!! You guessed correct number.")
    print("Your attempt is: ", counter)

