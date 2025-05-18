# 22. Capitalize the first letter of each word in a string

def capitalize(user_input):
    print(user_input.title())

def capitalize_words(user_input):
    words = user_input.split(' ') # returns a list
    capitalized_words = [word.capitalize() for word in words]
    return ' '.join(capitalized_words)


u_input = input("Enter a sentence: ")
capitalize(u_input)

capitalized_string = capitalize_words(u_input)
print("Capitalized string:",capitalized_string)