# 12. Define a global variable global_var = 10. Write a function that modifies a global variable value.

global_var=10

def modify_variable():
    global global_var
    global_var=6
    print(global_var)

modify_variable()
print(f"Outside function: {global_var}")