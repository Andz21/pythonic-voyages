# 11. Ask the user for a numerator and a denominator. Calculate the percentage and display it with
# two decimal places followed by a percent sign (e.g., 75.50%)

numerator = float(input("Enter the numerator: "))
denominator = float(input("Enter the denominator: "))

percentage = (numerator/denominator) * 100

print("The percentage is {}".format("%.2f" %percentage))