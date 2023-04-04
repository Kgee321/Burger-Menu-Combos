""" Component 3 -- Price Checker version 4
Adding onto Version 2 (not 3)
Converting float checker into a recyclable
function. Also converting into easygui.
Loop around function for testing purposes.
Written by Katelyn Gee
Create on 4/04/2022
"""

import easygui


# Recyclable functions for float checking
def price_checker(high, low, comment):
    # Loop for code to repeat in wrong input
    while True:

        try:
            # Ask for item price
            number = float(easygui.enterbox(comment, "Enter Number"))

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


while True:

    # Otherwise -- price is correct and program continues
    price = price_checker(50, 1, "Please enter the price of item: ")

    new_price = f"{price:.2f}"

    # Price outputted
    easygui.msgbox(f"${new_price} (2dp) is the price", "Price")
