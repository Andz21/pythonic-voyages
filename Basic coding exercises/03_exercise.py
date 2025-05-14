# 3. Print characters present at an even index number
# Write a Python code to accept a string from the user and display characters
# present at an even index number.
# For example, str = "PYnative". so your code should display ‘P’, ‘n’, ‘t’, ‘v’.

def print_even_chars(u_input):
    print("Printing only even index characters")
    for i in range(len(user_input)):
        if i % 2 == 0:
            print(user_input[i])

user_input = str(input("Enter a word: "))
print(f"Original string is {user_input}")

print_even_chars(user_input)


