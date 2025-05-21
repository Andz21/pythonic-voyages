# 21. Flatten a nested list using loops

nested_list = [1, [2, 3], [4, 5, 6], 7, [8, 9]]

flat_list = []

for item in nested_list:
    if isinstance(item,list):
        for i in item:
            flat_list.append(i)
    else:
        flat_list.append(item)

print("Flattened list: {}".format(flat_list))
