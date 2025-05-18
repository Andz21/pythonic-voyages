# 5. Check if the first and last numbers of a list are the same
# Write a code to return True if the list’s first and last numbers are the same.
# If the numbers are different, return False.

def is_first_and_last_match(num_list):
    if num_list[0] == num_list[len(num_list)-1]: #num_list[-1]
        return print("True")
    else:
        return print("False")

numbers_x = [10, 20, 30, 40, 10]
is_first_and_last_match(numbers_x)
