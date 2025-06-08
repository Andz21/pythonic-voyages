# Concatenation of 2 lists
list1 = [1,2,3]
list2 = [4,5,6]

for item in list1:
    list2.append(item)
print(list2)

print(list1 + list2)

# Can we pass function as an argument in python ?
# Yes. Higher-order functions are functions that can take other functions as arguments.

def add(x,y):
    return x + y

def apply_func(func,a,b):
    return func(a,b)

print(apply_func(add,5,2))

# What is dynamically typed language?
# the data type of the variable is determined at runtime not at compile time.
# Examples of dynamically typed language- python, javascript.
# Statically typed languages - C++, C,Java

# Python’s argument-passing model is neither “Pass by Value” nor “Pass by Reference” but it is “Pass by Object Reference”.
# Depending on the type of object you pass in the function, the function behaves differently.
# Immutable objects show “pass by value” whereas mutable objects show “pass by reference”.

# Lambda functi