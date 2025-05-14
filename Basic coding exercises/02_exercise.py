# 2. Print the sum of a current number and a previous number
# Write Python code to iterate through the first 10 numbers and,
# in each iteration, print the sum of the current and previous number.

def print_sum():
    for i in range(10):
        cur_num = i
        prev_num = i-1

        if prev_num == -1:
            prev_num = 0

        total = cur_num + prev_num
        print(f"Current number {cur_num} Previous number {prev_num} Sum: {total}")

print("Printing current and previous number sum in a range(10)")
print_sum()