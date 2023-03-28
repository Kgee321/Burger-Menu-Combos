""" This code is the same as 01_home_screen_v3 but a loop is around the code for testing.
Katelyn Gee
28/03/2023
"""

import easygui

# Loop for testing
while True:

    # Asking user what they want to do with the combos
    options = easygui.buttonbox("Enter what you would like to do with your combos: \n",
                                "Home Screen", choices=["Add", "Search", "Delete", "Print", "Exit"])
    print()

    # If user want to add combo
    if options == "Add":
        print("add() function is called on")

    # If user wants to find a combo
    elif options == "Search":
        print("search() function is called on")

    # If user wants to delete combo
    elif options == "Delete":
        print("delete() function is called on")

    # If user want to print combos
    elif options == "Print":
        print("print() function is called on")

    # If user want to leave code
    elif options == "Exit":

        # Goodbye message outputted
        easygui.msgbox("Goodbye!", "Leaving Screen")
        print("Program ends")




