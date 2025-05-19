# 9. Write a program to check if the given file is empty or not

import os

file_name = input("Enter the file to be checked: ")
size = os.stat(file_name).st_size
if size == 0:
    print('file is empty')
