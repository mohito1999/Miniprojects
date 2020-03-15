import random, sys
print("ROCK, PAPERS, SCISSORS!")
win = 0
losses = 0
ties = 0

while True: #loop for the entire game, game should always return to this
    print("Wins: " + str(win) + ", Losses: " + str(losses) + ", Ties: " + str(ties))
    while True: #loop for selection
        print("Make a selection: (r)ock, (p)aper, (s)cissor or (q)uit")
        user_choice = input()
        if user_choice == "q":
            sys.exit()
        if user_choice == 'r' or user_choice == 's' or user_choice == "p":
            break #break because if they have made a valid choice, you want them to return to the greater game loop.
    randNum = random.randint(1, 3)
    if randNum == 1:
        comp_move = 'r'
        print("ROCK")
    elif randNum == 2:
        comp_move = 'p'
        print("PAPER")
    elif randNum == 3:
        comp_move = 's'
        print("SCISSORS")
    if user_choice == comp_move:
        print("It's a tie!")
        ties = ties + 1
    elif user_choice == 'r' and comp_move == 'p':
        print("You lost!")
        losses = losses + 1
    elif user_choice == 'r' and comp_move == 's':
        print("You won!")
        win = win + 1
    elif user_choice == 'p' and comp_move == 'r':
        print("You won!")
        win = win + 1
    elif user_choice == "p" and comp_move == 's':
        print("You lost!")
        losses = losses + 1
    elif user_choice == 's' and comp_move == 'r':
        print("You lost!")
        losses = losses + 1
    elif user_choice == 's' and comp_move == 'p':
        print("You won!")
        win = win + 1
