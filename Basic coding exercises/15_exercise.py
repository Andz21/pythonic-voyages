# 15. Get an int value of base raises to the power of exponent

def calculate_exponent(base, exponent):
    result = 1
    for _ in range(1,exponent+1):
        result *= base

    return result



base = int(input("Enter the base: "))
exponent = int(input("Enter the exponent: "))
print(f"{base} raises to the power of {exponent} is: {calculate_exponent(base, exponent)}")