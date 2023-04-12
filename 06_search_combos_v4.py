""" Component 4 -- Search combos (version 4)
Adding onto function search_combos_v3.
This code asks user if they want to search again
or exit.
Also converts code into easygui
Written by Katelyn Gee
Created on the 05/04/2023
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

value = True
search_items = []

while True:
    # User enters search
    searching = easygui.enterbox("What combo or combo item are you looking for? ").title()

    # Loop to access all dictionary items
    for name_com, item_com in combos.items():

        # If search is in the combo name
        if searching in name_com:

            # Joining list together
            for i in item_com:
                items_print = ", ".join(item_com.keys())

            # printing results
            search_items.append(f"The combo named {name_com} contains {items_print}")
            value = False

        # Loop to access items in combo
        for item_name in item_com.keys():

            # If search is a combo item name
            if searching in item_name:
                search_items.append(f"{item_name} at a price of ${item_com[item_name]} is in the combo named {name_com}")
                value = False

    # Warning message if search not in combos
    if value:
        easygui.msgbox(f"Sorry, input {searching} is not in the combos")

    # Printing all search results
    else:
        # Joining search items together
        for i in search_items:
            search_total = f"\n".join(search_items)

        easygui.msgbox(f"Combos containing '{searching}' are \n{search_total}")

    # Asking if user wants to search again
    again = easygui.buttonbox("Do you want to search again or return to home screen?",
                              "Search options", choices=["Again", "Home Screen"])

    # if wanting to return home
    if again == "Home Screen":
        break
