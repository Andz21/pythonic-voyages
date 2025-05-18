# 7. Find the number of occurrences of a substring in a string
# Write a Python code to find how often the substring “Emma” appears in the given string.

str_x = "Emma is good developer. Emma is a writer"
substring = 'Emma'
count = 0

str_list = str_x.split()

for i in range(len(str_list)):
    if str_list[i] == substring:
        count += 1

print(f"Emma appeared {count} times in the string.")