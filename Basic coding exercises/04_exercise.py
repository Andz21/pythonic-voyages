# 4. Remove first n characters from a string
# Write a Python code to remove characters from a string from 0 to n and return a new string.

def remove_chars(word,n):
    for i in range(len(word)):
        if  i  > n-1:
            print(user_input[i])



user_input = str(input("Enter the word: "))
chars_to_remove = int(input("Enter characters to be removed: " ))

print("Removing characters from string")
remove_chars(user_input,chars_to_remove)