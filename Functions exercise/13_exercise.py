# Write a recursive function to calculate the factorial of a non-negative integer.

# Solution 1
def calculate_factorial(n):
    factorial = 1
    while n> 0:
        factorial *= n
        n = n-1
    print(factorial)

calculate_factorial(5)

# Solution 2
def factorial_recursive(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    elif n == 0:
        return 1  # Base case: factorial of 0 is 1
    else:
        return n * factorial_recursive(n - 1)  # Recursive step

# Example usage:
number = 5
result = factorial_recursive(number)
print(f"The factorial of {number} is {result}")