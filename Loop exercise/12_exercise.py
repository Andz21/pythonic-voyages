# 12. Display Fibonacci series up to 10 terms

n1 = 0
n2 = 1

print(n1, end= ' ')
print(n2, end = ' ')

for i in range(2,10):
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    print(n3, end = ' ')