import random

user_wins = 0
computer_wins = 0

options = ["rock","paper","scissors"]

while True:
    user = input("Type Rock/Paper/Scissors or Q to quit.").lower()
    if user == 'q':
        break
    
    if user not in options:
        continue

    random_number = random.randint(0,2)
    # rock: 0 , paper: 1, scissors: 2
    computer_pick = options[random_number]
    print("Computer picked", computer_pick +"." )

    if user == "rock" and computer_pick == "scissors":
        print("You won!")
        user_wins += 1
        continue

    elif user == "paper" and computer_pick == "rock":
        print("You won!")
        user_wins += 1
        continue

    elif user == "scissors" and computer_pick == "paper":
        print("You won!")
        user_wins += 1
        continue
    else:
        print("You lost!")
        computer_wins += 1


print("Your score is ",user_wins)
print("Computer score is ",computer_wins)
print("Good Bye")
