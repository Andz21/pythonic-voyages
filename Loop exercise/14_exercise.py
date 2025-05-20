# 14. Reverse a integer number

num = int(input("Enter a number: "))
reverse_num =0

while num != 0:
    rem = num % 10
    num //= 10
    reverse_num = (reverse_num * 10) + rem

print(f"Reverse number: {reverse_num}")