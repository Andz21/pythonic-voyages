# 4. Remove first n characters from a string
# Write a Python code to remove characters from a string from 0 to n and return a new string.

# Using slicing
# substring = s[start:end:step]
# s: The original string.
# start (optional): Starting index (inclusive). Defaults to 0 if omitted.
# end (optional): Stopping index (exclusive). Defaults to the end of the string if omitted.
# step (optional): Interval between indices. A positive value slices from left to right, while
#     a negative value slices from right to left. If omitted, it defaults to 1 (no skipping of characters).

def remove_chars(word, n):
    print('Original string:', word)
    x = word[n:]
    return x

print("Removing characters from a string")
print(remove_chars("pynative", 4))
print(remove_chars("pynative", 2))