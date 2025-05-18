# 7. Find the number of occurrences of a substring in a string
# Write a Python code to find how often the substring “Emma” appears in the given string.

str_x = "Emma is good developer. Emma is a writer"
substring = 'Emma'

count = str_x.count(substring)

print(f"Emma appeared {count} times in the string.")