import random
min = 1
max = 6

roll_again = "yes"

while roll_again == "yes":
    print("Dices are rolling")
    print(random.randint(min, max))
    print(random.randint(min, max))

    roll_again = input("would you like to roll again?")

if roll_again == "no":
    print("Thanks for using!")
