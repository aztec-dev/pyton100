"""
Day 4: 02/07/2024 (Catchup)
Title: Rock, Paper, Scissors
Project: create a rock, paper and scissors game using lists
"""
import random

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
player_answer = []
computer_answer = []
options = []
# Should the options be stored inside a list?
# I think it should as I consider it to be data.

options.append(rock)
options.append(paper)
options.append(scissors)

# Display player choice in ascii art
print("You chose:")
if player_choice == 0:
    print(options[0])
    player_answer.append(options[0])
    player_answer.append(0)
elif player_choice == 1:
    print(options[1])
    player_answer.append(options[1])
    player_answer.append(1)
elif player_choice == 2:
    print(options[2])
    player_answer.append(options[2])
    player_answer.append(2)

# Implement general computer logic. Use a random number to pick the index the computer will choose.
random_index = random.randint(0, len(options) - 1)
print("Computer chose:")
print(options[random_index])

if random_index == 0:
    computer_answer.append(options[0])
    computer_answer.append(0)
elif random_index == 1:
    computer_answer.append(options[1])
    computer_answer.append(1)
elif random_index == 2:
    computer_answer.append(options[2])
    computer_answer.append(2)

# Implement game logic
# Logic: 
# - Rock beats Scissors
# - Scissors beats Paper
# - Paper beats Rock

# Do we need a comparable
# Rock beats scissors
if player_answer[1] == 0 and computer_answer[1] == 2:
    print("You win!")
# Paper beats Rock
elif player_answer[1] == 1 and computer_answer[1] == 0:
    print("You win!")
# Scissors beats Paper
elif player_answer[1] == 2 and computer_answer[1] == 1:
    print("You win!")
# Draw
elif player_answer[1] == computer_answer[1]:
    print("It's a draw!")
else:
    print("You lose!")