# 15. Ask the user for a number. Print this number padded with leading zeros to a width of 5.
# For example, if the input is 12, the output should be “00012“

# Solution 1
num = int(input("Enter a number: "))
count = len(str(num))

num_with_zeroes = str(num)
if count < 5:
    zeroes = 5-count
    for _ in range(zeroes):
        num_with_zeroes = '0' + num_with_zeroes
    print(f"Number with leading zeroes : {num_with_zeroes}")
else:
    print(f"No leading zeroes. Original number {num}")

# Solution 2
number_str = input("Enter a number: ")
padded_number = number_str.zfill(5)
print(padded_number)
