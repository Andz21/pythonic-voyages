# 19. Print Full Multiplication Table

n = 10
for i in range(1,n+1):
    print(f"Multiplication table of: {i}")
    for j in range(1,11):
        print(i*j,end=' ')
    print('\n')