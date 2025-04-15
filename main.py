"""
This program calculates prices for custom house signs.
"""

# Start with the base price
charge = 35.00

# Ask the user for input
numChars = int(input("Enter the number of characters for the sign: "))
woodType = input("Enter the wood type (oak or pine): ").lower()
color = input("Enter the letter color (black, white, or gold): ").lower()

# Add $4 for each character after the first 5
if numChars > 5:
    charge = charge + (numChars - 5) * 4

# Add $20 if the sign is made of oak
if woodType == "oak":
    charge = charge + 20

# Add $15 if the color is gold
if color == "gold":
    charge = charge + 15

# Output the total charge
print("The charge for this sign is $" + str(charge))
