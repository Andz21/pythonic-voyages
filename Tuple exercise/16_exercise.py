# Given a tuple of numbers, create a new tuple where each number is squared.

t = (1, 2, 3, 4)
list1 = list(t)

new_list = [num**2 for num in list1]
squared_tuple_loop = tuple(new_list)

print(f"Squared tuple (loop): {squared_tuple_loop}")

# Using lambda
squared_tuple = tuple(map(lambda x: x**2,t))

print(f"Squared tuple: {squared_tuple}")