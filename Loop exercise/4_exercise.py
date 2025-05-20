# 4. Print multiplication table of a given number

num = int(input("Enter a number: "))
print(f"Multiplication table of {num} is: ")

for i in range(1,11,1):
    product = num * i
    print(product)