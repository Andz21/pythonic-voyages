# 1A. Create a string made of the first, middle and last character

str1 = "Dane"
str1_list = list(str1)
mid_letter = round(len(str1_list)/2)

for i in range(len(str1_list)):
    if i == 0:
        print(str1_list[i],end='')
    if i == mid_letter:
        print(str1_list[i],end='')
    if i == len(str1_list)-1:
        print(str1_list[i],end='')