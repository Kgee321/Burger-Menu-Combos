""" Base Component -- Version 1
Welcome screen and message created here
Pre-combos added to a dictionary inside a dictionary here
Adding each component as they are created
Not much editing done to the code
Adding code to add function so user cannot
make a new combo with the same name.
When input code entered, changing it to use
the char_boundary function.
Added components 1, 2, 3, and 4.
Written by Katelyn Gee
Created on the 28/03/2023
"""

import easygui


# Recyclable functions for float checking
def price_checker(high, low, comment, box_name):
    # Loop for code to repeat in wrong input
    while True:

        try:
            # Ask for item price
            number = float(easygui.enterbox(comment, box_name))

            # If item price out of boundary error
            if low > number or number > high:
                easygui.msgbox(f"Please enter a number between {low} and {high}. Try again",
                               "Out of Boundary")

            # Loop ends if input correct
            else:
                return number

        except ValueError:

            # When wrong input entered, question repeated
            easygui.msgbox("Input was not a float! Please enter a number", "Wrong Input Type")


# Function for finding
def char_boundary(upper, lower, question, box_name):
    while True:
        # Ask for the name of the combo
        asking = easygui.enterbox(question, box_name)

        # Upper string boundary
        if len(asking) > upper:
            easygui.msgbox(f"Wrong Input. Please enter less than {upper} letters", "Too Many Letters")

        # Lower string boundary
        elif len(asking) < (lower + 1):
            easygui.msgbox(f"Wrong Input. Please more than {lower} letters", "Not Enough Letters")

        # Input correct
        else:
            break

    return asking


# Function for adding a combo
def add():
    # Loop to restart code
    while True:

        # Setting Variables
        count = 0
        combo_items = {}
        new_combo = {}
        message = ""

        # Asking for combo name
        combo_name = char_boundary(10, 1, "Please enter combo name: ", "Combo name")
        combo_name = combo_name.title()

        # Finding if combo name already used
        if combo_name in combos.keys():
            easygui.msgbox("Name already a combo. Please choose a new name.")
            continue

        # Loop so 3 items can be added to combo
        while count != 3:

            # Adding to count variable
            count += 1

            # Asking for combo name
            item = char_boundary(20, 1, f"Please enter the name of item {count}: ", f"Item {count}")

            # Asking user to enter the price of that item
            price = price_checker(50, 1, f"Please enter the price of item {count}: ",
                                  f"Item {count}")
            price = f"{price:.2f}"

            # Adding item and price to dictionary
            combo_items[item] = price

        # Adding items to combo dictionary with combo name
        new_combo[combo_name] = combo_items

        # Formatting the dictionary
        for key, value in new_combo.items():
            message = f"{key}:\n"

            # Formatting dictionary inside dictionary
            for key2, value2 in value.items():
                message += f"{key2}: ${value2}, "

        # Outputting new combo and user clicks yes/no if correct/wrong combo
        answer1 = easygui.buttonbox(f"{message} \n\n Is this Combo Correct?", "New Combo Checking",
                                    choices=["Yes", "No"])

        # User enters yes
        if answer1 == "Yes":
            easygui.msgbox("Great! This New Combo was added", "New Combo Added")
            combos.update(new_combo)
            break

        # User enters no
        elif answer1 == "No":
            easygui.msgbox("Sorry, lets try again then!", "New Combo adding restarting")


# Function for joining values
def joining_values(lists, join_string):

    connected_output = ""

    # Loop to join list values
    for _ in lists:
        connected_output = join_string.join(lists)

    return connected_output


# Searching the combos functions
def search(action):
    # Values
    value = True
    search_items = []
    search_name = []

    while True:
        # User enters search
        searching = char_boundary(20, 0, f"Enter the combo or combo item you want to {action}: ",
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
            return True

        # Printing all search results
        else:

            return [searching, search_items, search_name]


# Delete combos functions
def delete():
    pass


# printing the menu function
def printing():
    pass


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

# Welcome Screen and instructions
easygui.msgbox("Welcome to Jim's Takeaways! \n"
               "You have the option to add combos, search combos, delete combos, "
               "or print the combo's menu in this program. Please select what you would "
               "like to do on the next page. \nEnjoy!", "Welcome and Instructions")

# Loop so code ends when user wants it to
while True:

    # Asking user what they want to do with the combos
    options = easygui.buttonbox("Enter what you would like to do with your combos: \n",
                                "Home Screen", choices=["Add", "Search", "Delete", "Print", "Exit"])

    # If user want to add combo
    if options == "Add":
        add()

    # If user wants to find a combo
    elif options == "Search":
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

    # If user wants to delete a combo
    elif options == "Delete":
        delete()

    # If user want to print combos
    elif options == "Print":
        printing()

    # If user want to leave code
    elif options == "Exit":

        # Goodbye message outputted and code ends
        easygui.msgbox("Goodbye! Thanks for using Jim's Takeaways", "Leaving Screen")
        break
