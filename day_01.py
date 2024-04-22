"""
Day 1: 23/04/2024
Title: Band Name Generator
Task: Create a program that generates a random name for the user based on the users city
and the users pet name.
"""

print("Welcome to the Band Name Generator.")

# get users city and pet name
city_name = input("What is the name of the city you grew up in? ").title()
pet_name = input("What is the name of your pet? ").title()

# Display band name
print(f"Your band name could be {city_name} {pet_name}'s")

