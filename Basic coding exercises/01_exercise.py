# 1. Calculate the multiplication and sum of 2 numbers
# Given two integer numbers, write a Python program to return their product
# only if the product is equal to or lower than 1000. Otherwise, return their sum.

from numpy import multiply

def multiply_or_sum(num1, num2):
    product = multiply(num1,num2)

    if product <= 1000:
        return print(f"The product of the numbers is: {product}")
    else:
        total = num1 + num2
        return print(f"The sum of the numbers is: {total}")

n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))

multiply_or_sum(n1, n2)