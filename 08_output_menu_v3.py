""" Component 6 -- Output Menu (version 3)
Changed the Deco so that it is more fun and creative
Tested this code against version 2 and agreed that
version 2's simpleness is better for this code.
This code will not be used in future program.
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
    message += f"~" * len(name_of_combo) + f"\n"

    # Loop to print dictionary inside the dictionary
    for item_in_combo, price_of_item in combo_items_price.items():

        # Combo item and its price printed
        message += f" * {item_in_combo}: ${price_of_item} \n"


easygui.msgbox(message, "Printing Menu")
