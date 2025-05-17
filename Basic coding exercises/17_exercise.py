# 17. Generate Fibonacci series up to 15 terms
# 0 1 1 2 3 5 8 13 21

f_num = 0
s_num = 1
print(f_num,end=' ')
print(s_num,end =' ')

for _ in range(1,14):
    next_num = f_num + s_num
    f_num = s_num
    s_num = next_num
    print(next_num,end = ' ')
