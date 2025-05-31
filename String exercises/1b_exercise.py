# 1B: Create a string made of the middle three characters

# Solution 1
str1 = "JhonDipPeta"

str1_list = list(str1)
mid_letter = int(len(str1_list)/2)

print(str1_list[mid_letter-1],end='')
print(str1_list[mid_letter],end='')
print(str1_list[mid_letter+1],end='')

# Solution 2
def get_middle_three_chars(str1):
    print("Original String is", str1)

    # first get middle index number
    mi = int(len(str1) / 2)

    # use string slicing to get result characters
    res = str1[mi - 1:mi + 2]
    print("Middle three chars are:", res)

get_middle_three_chars("JhonDipPeta")
get_middle_three_chars("JaSonAy")