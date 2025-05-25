# Create a function with keyword arguments
# The exercise requires you to create a function that
# can accept any number of keyword arguments. A keyword argument is where you
# specify the name of the argument along with its value
# (e.g., name="Alice", age=30). Inside the function,
# you need to access these arguments and print them in a key-value format.
from jsonpickle.util import items


def print_data(**kwargs):
    if kwargs:
        for key,value in items(kwargs):
            print(f"{key}:{value}")
    else:
        print("No values provided.")

print_data(name='Alice',age=30)
print_data()