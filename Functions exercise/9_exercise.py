# 9. Find the largest item from list

def largest_number(x):
    largest_num = x[0]
    for i in range(1,len(x)):
        if x[i] > largest_num:
            largest_num = x[i]

    return largest_num

x = [4, 6, 8, 24, 12, 2]
print(f"Largest number is: {largest_number(x)}")