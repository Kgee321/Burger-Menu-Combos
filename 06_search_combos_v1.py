""" Component 4 -- Search combos (version 1)
Asks user to enter what they want to search for
Outputs the combo that is in the search or an
error if the search is not a combo.
Only for key values of the dictionary.
Full pre saved dictionary added
Written by Katelyn Gee
Created on the 05/04/2023
"""

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

# User enters search
searching = input("What combo are you looking for? ").title()

# Finding that combo ask for in dictionary
if searching in combos.keys():
    print(f"The combo named {searching} is {combos[searching]}")
else:
    print("Sorry, input is not a combo name")

