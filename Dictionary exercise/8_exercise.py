# Print the value of key ‘history’ from nested dict

sampleDict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}

for key,value in sampleDict.items():
    for nested_key1,nested_value1 in value.items():
        for nested_key2, nested_value2 in nested_value1.items():
            if nested_key2 == 'marks':
                print(nested_value2.get('history'))

