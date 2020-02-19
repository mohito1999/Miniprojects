import random
min = int(input("Enter the lower bound: "))
max = int(input("Enter the upper bound: "))

num = random.randint(min, max)


guess = int(input("Enter your guess: "))

while guess != num:
    if guess > num:
        print("You guessed too high")
    if guess < num:
        print("You guessed too low")
    guess = int(input("Enter your guess: "))

if guess == num:
    print("Well done!")
