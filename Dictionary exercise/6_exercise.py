 # Given a string, create a dictionary where keys are characters and values are their frequencies in the string.

string1 = 'Jessa'
keys = list(string1)
values = []
for k in keys:
    values.append(string1.count(k))

my_dict = dict(zip(keys, values))
print(my_dict)