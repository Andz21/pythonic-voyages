# 11. Get each digit from a number in the reverse order.

def reverse_number(o_num):
    r_num = o_num[::-1]

    for i in range(len(r_num)):
        print(r_num[i], end=' ')

original_num = str(input("Enter a number:"))
print(f"The number in reverse: ")
reverse_number(original_num)