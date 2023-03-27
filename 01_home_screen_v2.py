""" This code is adding onto 01_home_screen_v1. It will put the code in a loop for when wrong
input entered as well as add .lower() so the capital answers to do matter
Katelyn Gee
27/03/2023
"""

# Loop repeats when wrong input entered
while True:

    # Asking user what they want to do with the combos
    options = input("Enter what you would like to do with your combos: \n"
                    "Enter Add to add a combo \n"
                    "Enter Search to search combos \n"
                    "Enter Delete to delete combos \n"
                    "Enter Print to print combos \n"
                    "Enter Exit to leave \n").lower()

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
        print("Wrong input entered \n ")
        continue

    # Code ends if user input was not a wrong input
    break



