# 20. Print Reverse Number Pattern
# 1 1 1 1 1
# 2 2 2 2
# 3 3 3
# 4 4
# 5

def print_pattern(n):
    for i in range(1,n+1):
        for j in range(i,n+1):
            print(i,end=' ')
        print('')

print_pattern(5)