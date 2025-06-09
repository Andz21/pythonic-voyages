# Create a dictionary by extracting the keys from a given dictionary
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

sample_dict1 = {}
for key,value in sample_dict.items():
    if key in ('name','salary'):
        sample_dict1.update({key:value})

print(sample_dict1)