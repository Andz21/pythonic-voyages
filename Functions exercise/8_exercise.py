# 8. Generate a Python list of all the even numbers between 4 to 30

def even_numbers():
    even_numbers_list = []
    for i in range(4,31):
        if i % 2 == 0:
            even_numbers_list.append(i)

    return even_numbers_list

print(f"Even numbers list: {even_numbers()}")