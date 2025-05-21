# 6. Count the total number of digits in a number

num = 75869

no_of_digits = 0
while num  != 0:
    num //= 10
    no_of_digits += 1

print(f"No. of digits: {no_of_digits}")