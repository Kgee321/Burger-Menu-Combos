"""Any code I am unsure of and I want to test, I do it here"""

# Pre Stored combos dictionary
combos = {
    "Value":
        {"Beef Burger": 5.69,
         "Fries": 1,
         "Fizzy drink": 1},
    "Cheezy":
        {"Cheeseburger": 6.69,
         "Fries": 1,
         "Fizzy drink": 1},
    "Super":
        {"Cheeseburger": 6.69,
         "Large fries": 2,
         "Smoothie": 2}
}

new_combo = {
    "Deluxe":
        {"Cheesy Sauce": 2.55,
         "Meat": 3.4,
         "Bun": 5.7}
}

# Combined dictionary's
combos.update(new_combo)
print(combos)

message = ""

for key, value in new_combo.items():
    message = f"{key}:\n"
    for key2, value2 in value.items():
        message += f"{key2}: {value2}, "

print(message)


