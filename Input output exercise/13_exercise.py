# 13. Ask the user for a word and a number.
# Print the word right-aligned in a field of width 20, followed by the number.
from pandas import concat

word = input("Enter a word: ")
num = input("Enter a number: ")

print(f"{word:>20}{num}")
