# Given a nested dictionary {'person': {'name': 'Alice', 'age': 30}}, print Alice’s age.

data = {'person': {'name': 'Alice', 'age': 30}}

print("Alice's age: ")
for key,value in data.items():
    for nested_key, nested_value in value.items():
        if nested_key == 'age':
            print(nested_value)