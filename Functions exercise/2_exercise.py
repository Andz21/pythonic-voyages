# 2. Create a function with variable length of arguments

def display_arguments(*args):
    for arg in args:
        print(arg)

display_arguments(10,20,30)
display_arguments('hello','guten tag')