# 12. Create a simple interactive menu with options like “1. Say Hello”,
# “2. Calculate Square”, “3. Exit”. Based on the user’s input, perform the corresponding action

def get_user_input():
    print("\nMenu:")
    print("1. Say Hello")
    print("2. Calculate Square")
    print("3. Exit")
    u_input = input("Select option 1, 2 or 3: ")
    if u_input not in ('1','2','3'):
        print("Invalid input ! Enter again.")
        u_input = get_user_input()
    return int(u_input)

def interactive_menu():
    user_input = get_user_input()
    while user_input != 3:
        if user_input == 1:
            print("Hello")
            user_input = get_user_input()
        elif user_input == 2:
            print("Calculate square")
            num = int(input("Enter a number: "))
            square = num * num
            print("Square = {}".format(square))
            user_input = get_user_input()

    print("Exit")

interactive_menu()
