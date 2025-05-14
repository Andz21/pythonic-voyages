# 6. Display numbers divisible by 5
# Write a Python code to display numbers from a list divisible by 5

def is_divisible(n_list):
    divisible_list = []
    for n in n_list:
        if n % 5 == 0:
            divisible_list.append(n)
    return divisible_list

num_list = [10, 20, 33, 46, 55]
print(f"Given list is: {num_list}")
result = is_divisible(num_list)

print(f"Divisible by 5: {result}")
