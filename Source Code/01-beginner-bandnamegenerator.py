# Create a greeting for your program.
# Ask the user for the city that they grew up in and store it in a variable.
# Ask the user for the name of a pet and store it in a variable.
# Combine the name of their city and pet and show them their band name.

print("Welcome to the Band Name Generator !")

country = input("What's the name of the city you grew up in ? \n").title()
pet_name = input("What's the name of your pet? \n").title()

print("Your band name could be ", country + " " + pet_name)
