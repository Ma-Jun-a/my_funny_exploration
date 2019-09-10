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
print(merge_sort(list_s))

# 不等长有序子列的归并排序

def sort_merge2(list):
    mid = int(len(list) / 2)

