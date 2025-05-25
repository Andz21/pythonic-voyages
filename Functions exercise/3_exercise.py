# 3. Return multiple values from a function
# Write a function calculation() that accepts two variables and calculates both their addition and subtraction.
# The function should then return both the sum and the difference in a single return statement.
from PIL.ImageChops import difference


def calculate(num1,num2):
    sum = num1 + num2
    if num1 > num2 :
        difference = num1 - num2
    difference = num2 - num1

    return sum, difference

sum, difference = calculate(10,50)

print(f'Sum: {sum}\nDifference: {difference}')