# 10. Merge two lists using the following condition

def merge_list(list1,list2):
    result_list = []
    for i in range(len(list1)):
        if list1[i] % 2 != 0:
            result_list.append(list1[i])

    for i in range(len(list2)):
        if list2[i] % 2 == 0:
            result_list.append(list2[i])

    return result_list

list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]
print("result list:", merge_list(list1, list2))
