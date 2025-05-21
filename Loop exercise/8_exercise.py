# 8. Print list in reverse order using a loop

# Solution 1
list1 = [10,20,30,40,50]

for n in range(len(list1)-1,-1,-1):
    print(list1[n])

# Solution 2
list1 = [10,20,30,40,50]
reverse_list = reversed(list1)

for item in reverse_list:
    print(item)



