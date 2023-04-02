""" Component 2 -- Add Combo Version 4
This codes is adding on from 02_add_combo_v2
Printing the dictionary with a nice format
Renamed some variables
Code restarts if the combo the user add is wrong
Adding letter limit on inputs
Written by Katelyn
Created on 2/04/2023
"""

import easygui

# Starting Dictionary that will have 3 combos already in it
combos = {}

# Loop to restart code
while True:

    # Setting Variables
    count = 0
    combo_items = {}
    new_combo = {}

    while True:
        # Ask for the name of the combo
        combo_name = easygui.enterbox("Please enter the name of the new combo: ", "Combo Name")

        # Upper string boundary
        if len(combo_name) > 10:
            easygui.msgbox("Wrong Input. Please enter less than 10 letters")

        # Lower string boundary
        elif len(combo_name) < 1:
            easygui.msgbox("Wrong Input. Please more than 1 letters")

        # Input correct
        else:
            break

    # Loop so 3 items can be added to combo
    while count != 3:

        # Adding to count variable
        count += 1

        while True:
            # Ask user to enter item name
            item = easygui.enterbox(f"Please enter the name of item {count}: ",
                                    f"Combo Item {count}")

            # Upper string boundary
            if len(item) > 20:
                easygui.msgbox("Wrong Input. Please enter less than 20 letters")

            # Lower string boundary
            elif len(item) < 1:
                easygui.msgbox("Wrong Input. Please more than 1 letters")

            # Input correct
            else:
                break

        # Asking user to enter the price of that item
        price = easygui.enterbox(f"Please enter the price of item {count}: \n",
                                 f"Combo Price {count}")

        # Adding item and price to dictionary
        combo_items[item] = price

    # Adding items to combo dictionary with combo name
    new_combo[combo_name] = combo_items

    # Formatting the dictionary
    for key, value in new_combo.items():
        message = f"{key}:\n"

        # Formatting dictionary inside dictionary
        for key2, value2 in value.items():
            message += f"{key2}: {value2}, "

    # Outputting new combo and user clicks yes/no if correct/wrong combo
    answer = easygui.buttonbox(f"{message} \n\n Is this Combo Correct?", "New Combo Checking",
                               choices=["Yes", "No"])

    # User enters yes
    if answer == "Yes":
        easygui.msgbox("Great! This New Combo was added", "New Combo Added")
        combos.update(new_combo)
        break

    # User enters no
    elif answer == "No":
        easygui.msgbox("Sorry, lets try again then!", "New Combo adding restarting")



