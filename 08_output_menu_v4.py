""" Component 6 -- Output Menu (version 3)
Converted code from version 2 into a
recyclable function for other parts of my code
and so it can be easily changed etc
This is the final code for this section
Written by Katelyn
Created on the 13/04/2023
"""

import easygui


# Function for connecting dictionaries to be printable
def output_menu(pattern, dictionary):

    message = ""

    # loop to print dictionary
    for name_of_combo, combo_items_price in dictionary.items():

        # Combo name printed
        message += f"\n{name_of_combo}\n"
        message += f"{pattern}" * (len(name_of_combo) * 2) + f"\n"

        # Loop to print dictionary inside the dictionary
        for item_in_combo, price_of_item in combo_items_price.items():

            # Combo item and its price printed
            message += f"{pattern} {item_in_combo}: ${price_of_item} \n"

    return message


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

# Output the menu
menu = output_menu("-", combos)
easygui.msgbox(menu, "Printing Menu")
