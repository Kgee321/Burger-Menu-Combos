""" Component 1 -- Home Screen version 3
This code is changing 01_home_screen_v2. Instead of input statements used, Easygui button box
is used to make code shorter and nicer for the user to use. A loop is also no longer needed as
there is no way the user can enter the wrong input.
Written by Katelyn Gee
Created on the 27/03/2023
"""

import easygui


# Asking user what they want to do with the combos
options = easygui.buttonbox("Enter what you would like to do with your combos: \n",
                            "Home Screen", choices=["Add", "Search", "Delete", "Print", "Exit"])

# If user want to add combo
if options == "Add":
    print("User wants to adds combo")

# If user wants to find a combo
elif options == "Search":
    print("User wants to search combos")

# If user wants to delete combo
elif options == "Delete":
    print("User wants to delete combo")

# If user want to print combos
elif options == "Print":
    print("User wants printed menu")

# If user want to leave code
elif options == "Exit":
    print("User wants to leave")




