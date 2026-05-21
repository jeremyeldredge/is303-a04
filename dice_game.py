"""
IS 303 A04 - Jeremy Eldredge

A simple dice game where the player rolls against the computer.

Inputs:
- user name (str)

Processes:
- import random
- dice_roll: random number from 1 to 6
- compare_scores: compares user score to computer score, returns winner
- scoreboard: accumulates total scores for user and computer across all rounds

Outputs:
- current round results
- current scoreboard
- roll again?
"""
import random

user_name = input("User name: ")
user_score = 0
computer_score = 0

def dice_roll():
    return random.choice([1,2,3,4,5,6])

def compare_scores(user_roll, computer_roll):
    if user_roll > computer_roll:
        return "You win!"
    elif computer_roll > user_roll:
        return "The computer won!"
    else:
        return "It's a tie!"

def scoreboard():
    print(f"Scoreboard - {user_name}: {user_score}, Computer: {computer_score}")


roll_again = "yes"
while roll_again == "yes":
    user_roll = dice_roll()
    computer_roll = dice_roll()
    print(f"You rolled a {user_roll} and the computer rolled a {computer_roll}")
    winner = compare_scores(user_roll, computer_roll)
    print(winner)
    if winner == "You win!":
        user_score += 1
    elif winner == "The computer won!":
        computer_score += 1
    scoreboard()
    while True:
        roll_again = input("Do you want to roll again? (yes/no) ")
        if roll_again in ["yes", "no"]:
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")



