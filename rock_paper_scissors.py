

## import modules
import random

## Declare variables
user_wins = 0
computer_wins = 0

## Declare options 0, 1, 2, 3
options = ["rock", "paper", "scissors", "test"]


## Start while loop
while True:
    user_input = input("Type Rock/Paper/scissors or Q to quit: ").lower()
    if user_input == 'q':
        break

    if user_input not in ["rock", "paper", "scissors"]:
        continue

    ## Rocker: 0, paper: 1, scissors: 2
    random_number = random.randint(0,2)

    computer_pick = options[random_number]
    print("Computer picked", computer_pick + ".")

    if user_input == "rock" and computer_pick == "scissors":
        print("you won!")
        user_wins += 1

    elif user_input == "paper" and computer_pick == "rock":
        print("you won!")
        user_wins += 1

    elif user_input == "scissors" and computer_pick == "paper":
        print("you won!")
        user_wins += 1

    else:
        print("you lost!")
        computer_wins += 1


print("You won " + str(user_wins) + " times")
print("Computer won " + str(computer_wins) + " times")
print("Goodbye!")