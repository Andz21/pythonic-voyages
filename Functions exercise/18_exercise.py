# 18. Create Higher-Order Function
# Write a function apply_operation(func, x, y) that takes a function func and two numbers x and y as arguments,
# and returns the result of calling func(x, y). Demonstrate its use with different functions (e.g., addition, subtraction).
# The exercise requires you to create a higher-order function, which is a function that can take other functions as arguments.

# Solution 1
def calculate(func,x,y):
    return func(x,y)

def addition(x,y):
    return x+y

subtract = lambda a, b: a - b
multiply = lambda a, b: a * b


result = calculate(subtract,5,2)

print(result)
