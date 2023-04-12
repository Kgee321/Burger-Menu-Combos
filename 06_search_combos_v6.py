""" Component 4 -- Search combos (version 6)
Converting search function into a recyclable code
so that it focus on searching for the item
Final code for component 4
Written by Katelyn Gee
Created on the 05/04/2023
"""

import easygui


# Joining lists together
def joining_values(lists, join_string):

    connected_output = ""

    # Loop to join list values
    for _ in lists:
        connected_output = join_string.join(lists)

    return connected_output


# Searching the combos
def search(items_or_not, action, extra_message):

    delete_items = []

    while True:
        # Values
        value = True
        search_items = []

        # User enters search
        searching = easygui.enterbox(f"Enter what you want to {action} in combos:",
                                     f"{action.title()} Combos").title()

        # Loop to access all dictionary items
        for name_com, item_com in combos.items():

            # If search is in the combo name
            if searching in name_com:

                # Joining list together
                items_print = joining_values(item_com.keys(), ", ")

                # printing results
                search_items.append(f"The combo named {name_com} contains {items_print}")
                delete_items.append(name_com)
                value = False

            # If deleting or searching items
            if items_or_not:

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

            # Results output and ask if this is correct to user
            correct = easygui.buttonbox(f"Combos containing '{searching}' are: \n{search_total}\n"
                                        f"{extra_message}", "Combo Search Results",
                                        choices=["Correct", "Incorrect"])

            # if incorrect, component/function restarts
            if correct == "Incorrect":
                easygui.msgbox("Sorry, lets try again! It may help if you refine your search "
                               "by adding as much letters as possible", f"{action} combos again")
                delete_items.pop(-1)
                continue

            # Combos found correct
            easygui.msgbox(f"Great! {action.title()} combo items has been completed!")

        # Asking if user wants to search again
        play_again = easygui.buttonbox(f"Do you want to {action} again or return to home screen?",
                                       "Search options", choices=["Again", "Home Screen"])

        # if wanting to return home
        if play_again == "Home Screen":
            return delete_items


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
search(True, "search", "Are these searched items correct?")


