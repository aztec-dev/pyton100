"""
Day 4: 02/07/2024 (Catchup)
Title: Rock, Paper, Scissors
Project: create a rock, paper and scissors game using lists
"""
import random

options = []

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

# Should the options be stored inside a list?
# I think it should as I consider it to be data.

options.append(rock)
options.append(paper)
options.append(scissors)

# Display player choice in ascii art
if player_choice == 0:
    print(options[0])
elif player_choice == 1:
    print(options[1])
elif player_choice == 2:
    print(options[2])

# Implement general computer logic. Use a random number to pick the index the computer will choose.
random_index = random.randint(0, len(options) - 1)
print("Computer chose:")
print(options[random_index])

# Implement game logic
# Logic: 
# - Rock beats Scissors
# - Scissors beats Paper
# - Paper beats Rock