# 10. Read Line Number 4 from File

with open('new_test.txt','r') as file:
    data = file.readlines()
    print(data[4])