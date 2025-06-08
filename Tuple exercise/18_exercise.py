# Sort a tuple of tuples by 2nd item
tuple1 = (('a', 23),('b', 37),('c', 11), ('d',29))
new_list = list(tuple1)

sorted_list = sorted(new_list, key=lambda item: item[1])
sorted_tuple = tuple(sorted_list)

print(f"Sorted tuple by 2nd item: {sorted_tuple}")