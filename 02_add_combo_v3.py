""" Component 2 -- Add Combo Version 3 (Trial 2)
This code is the same as Add Combo Version 2 but instead of
two easygui boxes for item and price, using one easygui box
and the split statement.
This works, but is not the most user-friendly
Written by Katelyn
Created on 2/04/2023
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

    # Ask user to enter item and price
    item_price = easygui.enterbox(f"Please enter the name of item {count} and its price. "
                                  f"Separate with a comma (,):",
                                  f"Combo Item {count}").split(",")

    # Adding item and price to dictionary
    combo_items[item_price[0]] = item_price[1]

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
