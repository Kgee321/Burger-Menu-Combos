""" Component 3 -- Price Checker version 1
This codes takes a float and checks if it is between
1 and 50. Using print statements and
if statements to find boundary's.
Converting float to 2dp
Loop for when wrong input entered
Written by Katelyn Gee
Create on 4/04/2022
"""

# Loop for code to repeat in wrong input
while True:

    # Ask users age
    price = float(input("Please enter the price of item: "))

    # If user age lower than 8
    if price < 0:
        print(f"${price} is not enough. Please enter a higher price.")
        print("Question Repeats\n")

    # If user age higher than 14
    elif price > 50:
        print(f"${price} is too much. Please enter a lower price.")
        print("Question Repeats\n")

    # Otherwise -- User is the right age to play
    else:
        print(f"${price:.2f} is the price")
        print("Program continues")
        break
