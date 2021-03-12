#归并排序
# 1. 等长有序子列的归并排序
list_s = range(1000)

def merge_sort(list):
    mid = int(len(list) / 2)
    sort_list = []
    for x in range(500):

        if list[x]<list[x + mid]:
            sort_list.append(list[x])
        else:
            sort_list.append(list[x + mid])
    return sort_list
# print(merge_sort(list_s))

# 不等长有序子列的归并排序
# list1 = [i for i in range(100)]
list3 = [1,3,5,9,88,777]
list4 = [7,8,9,10,11,15,47,99]
# list2 = [i for i in range(200,400)]
def sort_merge2(list1,list2):
    result = []
    i,j = 0,0
    while i<len(list1) and j<len(list2):
        if list1[i]<list2[j]:
            result.append(list1[i])
            i += 1
        else:
            result.append(list2[j])
            j += 1
    while i<len(list1):
        result.append(list1[i])
        i += 1
    while j<len(list2):
        result.append(list2[j])
        j += 1
    return result
# print(sort_merge2(list3,list4))

#分治法完成排序
list1 = [i for i in range(0,100000)]
def complicate_merge_sort(list):
    if len(list)<2:
        return list
    mid = int(len(list)/2)
    left = complicate_merge_sort(list[:mid])
    right = complicate_merge_sort(list[mid:])
    together = sort_merge2(left,right)
    return together
result = complicate_merge_sort(list1)
print(result)

