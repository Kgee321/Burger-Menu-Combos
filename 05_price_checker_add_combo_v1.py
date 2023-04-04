""" Component 2 and 3 Combining -- Version 1
This code will combine 04_price_checker_v4 and
03_Add_Combo_Function_v2 so that when the price
is asked for in add combo function, the float
checker function will be called on.
Making sure price rounded to 2dp
This code is the final code for components
2 and 3 and the code that will be added to
BC_base_v1
Written by Katelyn Gee
Create on 5/04/2023
"""

import easygui


# Recyclable functions for float checking
def price_checker(high, low, comment, box_name):
    # Loop for code to repeat in wrong input
    while True:

        try:
            # Ask for item price
            number = float(easygui.enterbox(comment, box_name))

            # If item price out of boundary error
            if low > number or number > high:
                easygui.msgbox(f"Please enter a number between {low} and {high}. Try again",
                               "Out of Boundary")

            # Loop ends if input correct
            else:
                return number

        except ValueError:

            # When wrong input entered, question repeated
            easygui.msgbox("Input was not a float! Please enter a number", "Wrong Input Type")


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
            price = price_checker(50, 1, f"Please enter the price of item {count}: ",
                                  f"Item {count}")
            price = f"${price:.2f}"

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

