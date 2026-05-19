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

def dice_roll():
    return random.choice([1,2,3,4,5,6])


user_name = input("User name: ")

roll_again = "yes"
while roll_again == "yes":
    print(f"You rolled a {dice_roll}")
    roll_again = input("Do you want to roll again? (yes/no) ")



