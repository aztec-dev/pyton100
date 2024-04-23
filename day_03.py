"""
Day 3: 23/04/2024 (Cathcup)
Title: Tip Calculator
Task: Create a treasure island game using if, else, elsif conditional statements.
"""

print("Welcome to Treasure Island! Your mission is to find the treasure.")
option = input("You come across a fork in the road. Do you go left or right?").title()

# Game start and conditional statements
if option == "Left":
    option = input("You come across a river. Do you swim or wait for a boat?").title()
    # This statement asks the user to swim or wait for a boat
    if option == "Wait":
        option = input("You waited by the river and a boat arrives, however, there are three doors on the boat. Do you pick the red, blue or yellow door? ").title()
        if option == "Red":
            print("You walk in the red door and suddenly consumed by fire from above. Game Over!") 
        elif option == "Blue":
            print("You walk in the blue door and suddenly devoured by a bear. Game Over!")
        elif option == "Yellow":
            print("You walk into the yellow door and safely travel to treasure island. You win!")
        else:
            print(f"You did {option} and realised that it was never a part of the choices. Game Over!")
    else:
         print("You are attacked by a trout. Game Over!")   
else:
    print("You fell into a hole. Game Over!")