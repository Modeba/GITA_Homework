import random

colors = ["red", "green", "blue", "yellow", "purple"]
guess  = None
secret = random.randint(0, len(colors) -1)
while True:
    # Print options
    for i in range(len(colors)):
        print(i + 1, colors[i])
    if input("Guess the color: ").lower() == colors[secret]:
        print("Correct!")
        break
    else:
        print("Incorrect, try again\n")