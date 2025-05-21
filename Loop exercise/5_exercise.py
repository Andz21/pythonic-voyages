# 5. Display numbers from a list using a loop
# The number must be divisible by five
# If the number is greater than 150, then skip it and move to the following number
# If the number is greater than 500, then stop the loop

numbers = [12, 75, 150, 180, 145, 525, 50]

for num in numbers:
    if num % 5 == 0 and num <= 150:
        print(num)
    elif num > 500:
        break