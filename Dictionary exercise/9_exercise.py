# In the below dictionary, change name to ‘Jessa’.

nested_student_dict = {
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

nested_student_dict['class']['student']['name'] = 'Jessa'
print(nested_student_dict)