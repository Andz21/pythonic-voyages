# 6. Write a program to create a recursive function that calculates the sum of numbers from 0 to 10.
#
# A recursive function is a function that calls itself repeatedly.

def calculate_sum(num):
    if num:
        return num + calculate_sum(num-1)
    else:
        return 0

res = calculate_sum(10)
print(res)

