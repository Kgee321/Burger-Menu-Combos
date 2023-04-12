""" Component 6 -- Output Menu (version 2)
Converted to easygui
And formatting code so it looks formal
and has basic but formal decor
Written by Katelyn
Created on the 13/04/2023
"""

import easygui

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

message = ""

# loop to print dictionary
for name_of_combo, combo_items_price in combos.items():

    # Combo name printed
    message += f"\n{name_of_combo}\n"
    message += f"-" * (len(name_of_combo) * 2) + f"\n"

    # Loop to print dictionary inside the dictionary
    for item_in_combo, price_of_item in combo_items_price.items():

        # Combo item and its price printed
        message += f" - {item_in_combo}: ${price_of_item} \n"


easygui.msgbox(message, "Printing Menu")
