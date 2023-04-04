""" Component 3 -- Price Checker version 3
Same code as version 2 but rearranged code
so while loop used instead of if statement.
Trial with version 2 and conclude that v2 is
better, therefore, this code will not be used
in future in codes.
Written by Katelyn Gee
Create on 4/04/2022
"""

# Variable setting
price = 0

# Loop for code to repeat in wrong input
while not 1 < price < 50:

    try:
        # Ask for item price
        price = float(input("Please enter the price of item: "))

    except ValueError:

        # When wrong input entered, question repeated
        print("Not a float! Please enter a number")


# Otherwise -- price is correct and program continues
print(f"${price:.2f} (2dp) is the price")


