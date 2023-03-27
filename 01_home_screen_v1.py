""" This code is the beginning of creating burger combos home screen. This code will not
use easygui to begin with and print statements will be used and deleted later to
test if code is working.
Katelyn Gee
27/03/2023
"""

# Asking user what they want to do with the combos
options = input("Enter what you would like to do with your combos: \n"
                "Enter Add to add a combo \n"
                "Enter Search to search combos \n"
                "Enter Delete to delete combos \n"
                "Enter Print to print combos \n"
                "Enter Exit to leave \n")

# If user want to add combo
if options == "add":
    print("User wants to adds combo")

# If user wants to find a combo
elif options == "search":
    print("User wants to search combos")

# If user wants to delete combo
elif options == "delete":
    print("User wants to delete combo")

# If user want to print combos
elif options == "print":
    print("User wants printed menu")

# If user want to leave code
elif options == "exit":
    print("User wants to leave")

# If an incorrect code entered
else:
    print("Wrong input entered")



