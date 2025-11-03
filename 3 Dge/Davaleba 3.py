import random

secret_number = random.randint(1, 10)
guess = None
while guess != secret_number:
    guess = int(input())
    if guess > secret_number:
        print("Too high ")
    if guess < secret_number:
        print("Too low ")

print("You win ")