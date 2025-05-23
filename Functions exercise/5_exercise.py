# 5. Create a program with nested functions to perform an addition calculation as follows:
#
# Define an outer function that accepts two parameters, a and b.
# Inside this outer function, define an inner function that calculates the sum of a and b.
# The outer function should then add 5 to this sum.
# Finally, the outer function should return the resulting value.”

def addition_calculation(num1,num2):
    def addition(n1,n2):
        total = n1 + n2
        return total

    sum = addition(num1, num2)
    addition_total = sum + 5
    return addition_total

total = addition_calculation(10,20)
print(f'Sum : {total}')