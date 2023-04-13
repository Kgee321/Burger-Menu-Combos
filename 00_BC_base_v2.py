""" Base Component -- Version 1
Adding components 4, 5 and 6
Some function names changed
Editing any mistakes
Adding in functions anywhere they can go
Written by Katelyn Gee
Created on the 12/04/2023
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
        asking = easygui.enterbox(question, box_name).title()

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

        combo_message = output_menu("-", new_combo)

        # Outputting new combo and user clicks yes/no if correct/wrong combo
        answer1 = easygui.buttonbox(f"{combo_message} \nIs this Combo Correct?", "New Combo Checking",
                                    choices=["Yes", "No"])

        # User enters yes
        if answer1 == "Yes":
            easygui.msgbox("Great! This New Combo was added", "New Combo Added")
            combos.update(new_combo)
            break

        # User enters no
        elif answer1 == "No":
            easygui.msgbox("Sorry, lets try again then!", "New Combo adding restarting")


# Joining lists together
def joining_values(lists, join_string):

    connected_output = ""

    # Loop to join list values
    for _ in lists:
        connected_output = join_string.join(lists)

    return connected_output


# Searching the combos functions
def search_delete(items_or_not, action, extra_message):

    delete_items = []

    while True:
        # Values
        value = True
        search_items = []

        # User enters search
        searching = char_boundary(20, 0, f"Enter what you want to {action} in combos:",
                                  f"{action.title()} Combos").title()

        # Loop to access all dictionary items
        for name_com, item_com in combos.items():

            # If search is in the combo name
            if searching in name_com:

                # Joining list together
                items_print = joining_values(item_com.keys(), ", ")

                # Printing results
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
        search_delete(True, "search", "Are these searched items correct?")

    # If user wants to delete a combo
    elif options == "Delete":

        # Calling on function for deleting dictionary
        answer = search_delete(False, "delete", "Do you want to delete this combo?")

        # Checking if there are items in the list
        if len(answer) > 0:

            # Combo names that are in search results
            for a in range(len(answer)):

                # Deleting that combo
                del combos[answer[a]]

    # If user want to print combos
    elif options == "Print":
        menu = output_menu("-", combos)
        easygui.msgbox(menu, "Printing Menu")

    # If user want to leave code
    elif options == "Exit":

        # Goodbye message outputted and code ends
        easygui.msgbox("Goodbye! Thanks for using Jim's Takeaways", "Leaving Screen")
        break
