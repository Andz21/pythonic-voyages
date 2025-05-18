# 5. Accept a list of 5 float numbers as an input from the user

def float_numbers():
    numbers = []
    for _ in range(1,6):
        num = float(input("Enter a float number: "))
        numbers.append(num)

    print("The list of numbers are: {}".format(numbers))

float_numbers()
