# 22. Find largest and smallest digit in a number


def find_largest_and_smallest_digit(num1):
    if num1 == 0:
        print("The number is zero. Largest and smallest digit is 0.")
    if num1 < 0:
        num1 = abs(num1)
    largest_number = 0
    smallest_number = 9
    while num1 != 0:
        rem = num1 % 10
        num1 //= 10
        if rem > largest_number:
            largest_number = rem
        if rem < smallest_number:
            smallest_number = rem

    print(largest_number)
    print(smallest_number)

num = -5082
find_largest_and_smallest_digit(num)