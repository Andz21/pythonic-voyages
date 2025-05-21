# 20. Print the alternate numbers pattern
# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15

# n = 15
# for i in range(1,n):
#     if i <= 2:
#         for j in range(0,i):
#             print(i+j,end=' ')
#         print('')
#     if i == 3:
#         for j in range(1,i+1):
#             print(i+j,end=' ')
#         print('')
#     if i == 4:
#         for j in range(3,i+3):
#             print(i+j,end=' ')
#         print('')
#     if i == 5:
#         for j in range(6,i+6):
#             print(i+j,end=' ')
#         print('')
#     if i == 6:
#         for j in range(10,i+10):
#             print(i+j,end=' ')
#         print('')


def print_alternate_pattern(rows):
    num = 1
    for i in range(1, rows + 1):
        if i % 2 != 0: # Odd row: increasing order
            for x in range(num, num + i):
              print(x, end=' ')
            print() # to display next row of number on new line
        else: # Even row: decreasing order
            for y in range(num + i - 1, num - 1, -1):
              print(y, end=' ')
            print() # # to display next row of number on new line
        num += i

# Call the function to print the pattern with a specified number of rows
print_alternate_pattern(5)