""" Base Component -- Version 1
Welcome screen and message created here
Pre-combos added to a dictionary inside a dictionary here
Adding each component as they are created
Not much editing done to the code
Written by Katelyn Gee
Created on the 28/03/2023
"""

import easygui


# Adding a new combo function
def add():
    pass


# Searching the combos functions
def search():
    pass


# Delete combos functions
def delete():
    pass


# printing the menu function
def printing():
    pass


# Pre Stored combos dictionary
combos = {
    "Value":
        {"Beef Burger": 5.69,
         "Fries": 1,
         "Fizzy drink": 1},
    "Cheezy":
        {"Cheeseburger": 6.69,
         "Fries": 1,
         "Fizzy drink": 1},
    "Super":
        {"Cheeseburger": 6.69,
         "Large fries": 2,
         "Smoothie": 2}
}

# Welcome Screen and instructions
easygui.msgbox("Welcome to Jim's Takeaways! \n"
               "You have the option to add combos, search combos, delete combos, "
               "or print the combo's menu in this program. Please select what you would "
               "like to do on the next page. \nEnjoy!", "Welcome and Instructions")

# Loop so code ends when user wants it to
while True:

    # Asking user what they want to do with the combos
    options = easygui.buttonbox("Enter what you would like to do with your combos: \n",
                                "Home Screen", choices=["Add", "Search", "Delete", "Print", "Exit"])

    # If user want to add combo
    if options == "Add":
        add()

    # If user wants to find a combo
    elif options == "Search":
        search()

    # If user wants to delete combo
    elif options == "Delete":
        delete()

    # If user want to print combos
    elif options == "Print":
        printing()

    # If user want to leave code
    elif options == "Exit":

        # Goodbye message outputted and code ends
        easygui.msgbox("Goodbye! Thanks for using Jim's Takeaways", "Leaving Screen")
        break
