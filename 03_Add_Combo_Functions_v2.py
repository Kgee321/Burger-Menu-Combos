""" Component 2 -- Add Combo Functions version 2
Converting the whole code into a function, so it will
be placed into BC_Base code.
This is the code I used for testing.
Final code for component 2.
Written by Katelyn
Created on 3/04/2023
"""

import easygui


# Function for finding
def char_boundary(upper, lower, question, box_name):
    while True:
        # Ask for the name of the combo
        asking = easygui.enterbox(question, box_name)

        # Upper string boundary
        if len(asking) > upper:
            easygui.msgbox(f"Wrong Input. Please enter less than {upper} letters", "Too Many Letters")

        # Lower string boundary
        elif len(asking) < (lower + 1):
            easygui.msgbox(f"Wrong Input. Please more than {lower} letters", "Not Enough Letters")

        # Input correct
        else:
            break

    return asking


# Function for adding a combo
def add():
    # Loop to restart code
    while True:

        # Setting Variables
        count = 0
        combo_items = {}
        new_combo = {}
        message = ""

        # Asking for combo name
        combo_name = char_boundary(10, 1, "Please enter combo name: ", "Combo name")

        # Loop so 3 items can be added to combo
        while count != 3:

            # Adding to count variable
            count += 1

            # Asking for combo name
            item = char_boundary(20, 1, f"Please enter the name of item {count}: ", f"Item {count}")

            # Asking user to enter the price of that item
            price = easygui.enterbox(f"Please enter the price of item {count}: \n",
                                     f"Item {count}")

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


# Starting Dictionary that will have 3 combos already in it
combos = {}

# Function called on
add()
