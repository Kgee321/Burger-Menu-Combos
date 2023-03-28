""" This code is removing the print statements and replacing them with functions calls.
The functions that are being called on have also been added although, they have nothing
in them yet (or just pass). Also testing loop has been removed as not needed in final
code. Final code for home_screen and will be in the base component.
Katelyn Gee
28/03/2023
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


# Asking user what they want to do with the combos
options = easygui.buttonbox("Enter what you would like to do with your combos: \n",
                            "Home Screen", choices=["Add", "Search", "Delete", "Print", "Exit"])
print()

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

    # Goodbye message outputted
    easygui.msgbox("Goodbye!", "Leaving Screen")





