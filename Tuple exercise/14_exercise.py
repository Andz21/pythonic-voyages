# Removing Duplicates from Tuple
from itertools import count

my_tuple = (1, 2, 2, 3, 4, 4, 5)

new_list = []
for element in my_tuple:
    if element not in new_list:
        new_list.append(element)

unique_tuple = tuple(new_list)

print(f"Original tuple with duplicates: {my_tuple}")
print(f"Tuple with unique elements: {unique_tuple}")



