""" Component 4 -- Search combos (version 2)
Added in the option for the user to search for
items in the combo and all results with that item
are outputted.
Because I used a for loop, code can find the start
of combo name. For example,
'val' recognised as value combo.
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

    # Loop to access items in combo
    for item_name in item_com.keys():

        # If search is a combo item name
        if searching in item_name:
            print(f"The {item_name} at a price of ${item_com[item_name]} is in the combo named {name_com}")

    # If search not in dictionary
    else:
        counting += 1 # FIX

# Warning message if search not in combos
if counting == len(combos):
    print("Sorry, input not in the combos")

