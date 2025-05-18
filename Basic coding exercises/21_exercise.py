# 21. Check if a user-entered string contains any digits using a for loop

def is_contain_digit(user_input):
    for i in range(len(user_input)):
        if user_input[i] in ('0','1','2','3','4','5','6','7','8','9'):
            return True
    return False


u_input = input("Enter a string: ")
result = is_contain_digit(u_input)
if result:
    print("The string contains atleast one digit.")
else:
    print("The string does not contain any digits.")