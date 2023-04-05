""" Component 4 -- Search combos (version 2)
Ask if user want to search again or exit
back to home screen.
Written by Katelyn Gee
Created on the 05/04/2023
"""

# Pre Stored combos dictionary
combos = {
    "Value":
        {"Beef Burger": 5.69,
         "Fries": 1,
         "Fizzy Drink": 1},
    "Cheezy":
        {"Cheeseburger": 6.69,
         "Fries": 1,
         "Fizzy Drink": 1},
    "Super":
        {"Cheeseburger": 6.69,
         "Large Fries": 2,
         "Smoothie": 2}
}

counting = 0

# User enters search
searching = input("What combo or combo item are you looking for? ").title()

# Loop to access all dictionary items
for name_com, item_com in combos.items():

    # If search is in the combo name
    if searching in name_com:
        print(f"The combo named {name_com} is {item_com}")

    # If search is a combo item name
    elif searching in item_com.keys():
        print(f"The {searching} at a price of ${item_com[searching]} is in the combo named {name_com}")

    # If search not in dictionary
    else:
        counting += 1

# Warning message if search not in combos
if counting == len(combos):
    print("Sorry, input not in the combos")

