# 7. Print the following pattern
# 5 4 3 2 1
# 4 3 2 1
# 3 2 1
# 2 1
# 1

n = 6
for i in range(n,0,-1):
    for j in range(i,0,-1):
        print(j,end=' ')
    print('')