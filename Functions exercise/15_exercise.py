# 15.Use a lambda with the filter() function to get all even numbers from a list

# Solution 1
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

is_even_number = lambda x: x%2==0
filtered = filter(is_even_number,numbers)
even_numbers = []
for num in filtered:
    even_numbers.append(num)

print("Even numbers =",even_numbers)

# Solution 2
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(f"The even numbers in the list are: {even_numbers}")