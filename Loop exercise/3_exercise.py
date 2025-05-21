# 3. Calculate sum of all numbers from 1 to a given number

num = int(input("Enter a number: "))

sum = 0
for i in range(num+1):
    sum += i

print(f"Sum of the numbers: {sum}")