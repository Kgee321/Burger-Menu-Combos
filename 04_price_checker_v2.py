""" Component 3 -- Price Checker version 2
Adding onto Version 1.
Putting a try loop into the code to stop code
from crashing when non float entered.
Changing inputs to easygui.
Removing unnecessary print statements
Combining if statements to shorten code
Written by Katelyn Gee
Create on 4/04/2022
"""

# Loop for code to repeat in wrong input
while True:

    try:
        # Ask for item price
        price = float(input("Please enter the price of item: "))

        # If item price out of boundary error
        if 1 > price or price > 50:
            print(f"Price needs to be between 1 and 50. Try again")

        # Loop ends if input correct
        else:
            break

    except ValueError:

        # When wrong input entered, question repeated
        print("Not a float! Please enter a number")

# Otherwise -- price is correct and program continues
print(f"${price:.2f} (2dp) is the price")
