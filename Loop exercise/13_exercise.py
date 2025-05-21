# 13. Find the factorial of a given number

num = int(input("Enter a number: "))

factorial = 1
for i in range(num,0,-1):
    factorial *= i

print(f"Factorial : {factorial}")