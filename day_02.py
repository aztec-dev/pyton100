"""
Day 2: 23/04/2024 (Cathcup)
Title: Tip Calculator
Task: Create a tip calculator that calculates the tip amount based on the total bill and the
percentage of the tip.
"""

print("Welcome to the tip calculator.")

bill = float(input("What was the total bill? $"))

tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? %"))
number_of_people = int(input("How many people to split the bill? "))
total_bill = (bill / number_of_people) * (1 + (tip_percentage / 100))
print(f"Each person should pay: ${total_bill:.2f}")