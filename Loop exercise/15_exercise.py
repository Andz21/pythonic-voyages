# 15. Print elements from a given list present at odd index positions

# Solution 1
my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

for i in range(len(my_list)):
    if i % 2 != 0:
        print(my_list[i], end= ' ')


# Solution 2
my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# stat from index 1 with step 2( means 1, 3, 5, an so on)
for i in my_list[1::2]:
    print(i, end=" ")