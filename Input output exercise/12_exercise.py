# 12. Create a simple interactive menu with options like “1. Say Hello”,
# “2. Calculate Square”, “3. Exit”. Based on the user’s input, perform the corresponding action

def get_user_input():
    u_input = int(input("Select option 1, 2 or 3: "))
    return u_input

while get_user_input() != 3:
    if get_user_input() == 1:
        print("Hello")
        get_user_input()
    elif u_input == 2:
        print("Calculate square")
        num = int(input("Enter a number: "))
        square = num * num
        print("Square = {}".format(square))

print("Exit")
