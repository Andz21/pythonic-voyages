# Delete a list of keys from a dictionary
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}

sample_dict.pop('name')
sample_dict.pop('salary')
print(sample_dict)

# keys = ["name", "salary"]
#
# sample_dict = {k: sample_dict[k] for k in sample_dict.keys() - keys}