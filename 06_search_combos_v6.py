""" Component 4 -- Search combos (version 4)
Converting search function into a recyclable code
so that it focus on searching for the item
Final code for component 4
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


def search(action):
    # Values
    value = True
    search_items = []
    search_name = []

    while True:
        # User enters search
        searching = easygui.enterbox(f"Enter the combo or combo item you want to {action}: ",
                                     f"{action} combos").title()

        # Loop to access all dictionary items
        for name_com, item_com in combos.items():

            # If search is in the combo name
            if searching in name_com:

                # Joining list together
                items_print = joining_values(item_com.keys(), ", ")

                # printing results
                search_name.append([name_com, items_print])
                value = False

            # Loop to access items in combo
            for item_name in item_com.keys():

                # If search is a combo item name
                if searching in item_name:
                    search_items.append([item_name, item_com[item_name], name_com])
                    value = False

        # Warning message if search not in combos
        if value:
            easygui.msgbox(f"Sorry, input {searching} is not in the combos",
                           "Search not in Combos")

        # Printing all search results
        else:

            return [searching, search_items, search_name]


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
while True:

    # Search function
    answer = search("Search")
    output_search = ""

    # If search not in combos
    if answer:
        pass

    # If search results in combos
    else:

        # Items that are in search results
        for i in range(len(answer[1])):

            output_search += f"{answer[1][i][0]} which costs ${answer[1][i][1]} and is in combo "\
                             f"{answer[1][i][2]} \n"

        # Combo names that are in search results
        for a in range(len(answer[2])):
            output_search += f"The combo name {answer[2][a][0]} which contains {answer[2][a][1]}.\n"

        # Output search results
        easygui.msgbox(f"The search '{answer[0]}' is in: \n{output_search}", "Combo Search Results")

    # User wants to search again or leave to home screen
    again = easygui.buttonbox(f"Do you want to search again or return to home screen?",
                              "Again or Home Screen", choices=["Again", "Home Screen"])

    # If wanting to return home
    if again == "Home Screen":
        break



