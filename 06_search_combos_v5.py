""" Component 4 -- Search combos (version 5)
Converting code into a basic function
also creating a recyclable joinning function that
can be used in other parts of future and
previous components
Written by Katelyn Gee
Created on the 05/04/2023
"""

import easygui


def joining_values(lists, join_string):

    connected_output = ""

    # Loop to join list values
    for _ in lists:
        connected_output = join_string.join(lists)

    return connected_output


def search():

    while True:
        # Values
        value = True
        search_items = []

        # User enters search
        searching = easygui.enterbox("What combo or combo item are you looking for? ", "Searching Combos").title()

        # Loop to access all dictionary items
        for name_com, item_com in combos.items():

            # If search is in the combo name
            if searching in name_com:

                # Joining list together
                items_print = joining_values(item_com.keys(), ", ")

                # printing results
                search_items.append(f"The combo named {name_com} contains {items_print}")
                value = False

            # Loop to access items in combo
            for item_name in item_com.keys():

                # If search is a combo item name
                if searching in item_name:
                    search_items.append(f"{item_name} at a price of ${item_com[item_name]} is "
                                        f"in the combo named {name_com}")
                    value = False

        # Warning message if search not in combos
        if value:
            easygui.msgbox(f"Sorry, input {searching} is not in the combos", "Search not in Combos")

        # Printing all search results
        else:
            # Joining search items together
            search_total = joining_values(search_items, "\n")

            easygui.msgbox(f"Combos containing '{searching}' are: \n{search_total}",
                           "Combo Search Results")

        # Asking if user wants to search again
        again = easygui.buttonbox("Do you want to search again or return to home screen?",
                                  "Search options", choices=["Again", "Home Screen"])

        # if wanting to return home
        if again == "Home Screen":
            break


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

# Calling on function for searching dictionary
search()
