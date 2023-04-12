""" Component 6 -- Output Menu (version 1)
Created a for loop to print the combos
Written by Katelyn
Created on the 13/04/2023
"""

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

# loop to print dictionary
for name_of_combo, combo_items_price in combos.items():

    # Combo name printed
    print(f"{name_of_combo}:\n")

    # Loop to print dictionary inside the dictionary
    for item_in_combo, price_of_item in combo_items_price.items():

        # Combo item and its price printed
        print(f"{item_in_combo}: ${price_of_item}")

    print()
