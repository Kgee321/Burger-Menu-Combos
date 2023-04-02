""" Component 2 -- Add Combo Version 2 (Trial 1)
Converting the print function to easygui
Adding the values the user inputted into a dictionary
At end of code, outputing the values and checking
with the user if the code is correct.
Written by Katelyn
Created on 1/04/2023
"""

import easygui

# Setting Variables
count = 0
combos = {}
combo_items = {}

# Ask for the name of the combo
combo_name = easygui.enterbox("Please enter the name of the new combo: ", "Combo Name")

# Loop so 3 items can be added to combo
while count != 3:

    # Adding to count variable
    count += 1

    # Ask user to enter item name
    item = easygui.enterbox(f"Please enter the name of item {count}: ",
                            f"Combo Item {count}")

    # Asking user to enter the price of that item
    price = easygui.enterbox(f"Please enter the price of item {count}: ",
                             f"Combo Price {count}")

    # Adding item and price to dictionary
    combo_items[item] = price

# Adding items to combo dictionary with combo name
combos[combo_name] = combo_items

# Outputting new combo and user clicks yes/no if correct/wrong combo
answer = easygui.buttonbox(f"{combos} \n\n Is this Combo Correct?", "New Combo Checking",
                           choices=["Yes", "No"])

# User enters yes
if answer == "Yes":
    easygui.msgbox("Combo is correct! ", "Correct")

# User enters no
elif answer == "No":
    easygui.msgbox("Combo is wrong", "Wrong")
