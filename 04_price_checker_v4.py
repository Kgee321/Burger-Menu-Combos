""" Component 3 -- Price Checker version 4
Adding onto Version 2 (not 3)
Converting float checker into a recyclable
function. Also converting into easygui.
Written by Katelyn Gee
Create on 4/04/2022
"""

import easygui


# Recyclable functions for float checking
def price_checker(high, low):
    # Loop for code to repeat in wrong input
    while True:

        try:
            # Ask for item price
            number = float(easygui.enterbox("Please enter the price of item: "))

            # If item price out of boundary error
            if low > number or number > high:
                easygui.msgbox(f"Price needs to be between {low} and {high}. Try again")

            # Loop ends if input correct
            else:
                return number

        except ValueError:

            # When wrong input entered, question repeated
            easygui.msgbox("Not a float! Please enter a number")


# Otherwise -- price is correct and program continues
price = price_checker(50, 1)

easygui.msgbox(f"${price:.2f} (2dp) is the price")
