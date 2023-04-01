""" Component 2 -- Add Combo version 1
Asking the user to add the combo name
Not using Easygui yet but print statements
Looping the item and price 3 times for 3 items
Written by Katelyn
Created on 1/04/2023
"""

# Setting Variables
count = 0

# Ask for the name of the combo
combo_name = input("Please enter the name of the new combo: ")

# Loop so 3 items can be added to combo
while count != 3:

    # Adding to count variable
    count += 1

    # Ask user to enter item name
    item = input(f"Please enter the name of item {count}: ")

    # Asking user to enter the price of that item
    price = float(input(f"Please enter the price of item {count}: "))

# Goodbye message
print("Program moves on")
