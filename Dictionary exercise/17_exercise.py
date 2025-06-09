# Write a code to swap keys and values in a dictionary. Assume all values are unique

original_dict1 = {'a': 1, 'b': 2, 'c': 3}
print('original dictionary',original_dict1)

new_dict_values = original_dict1.keys()
new_dict_keys = original_dict1.values()

new_dict = dict(zip(new_dict_keys,new_dict_values))
print('Inverted dictionary',new_dict)