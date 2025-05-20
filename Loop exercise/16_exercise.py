# 16. Calculate the cube of all numbers from 1 to a given number

input_number = int(input("Enter a number: "))

for num in range(1,input_number+1):
    cube = pow(num,3)
    print(f"Current number is : {num} and cube is : {cube}")
