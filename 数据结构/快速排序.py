import random
def generate_unsorted():
    my_list = []
    for i in range(1000):
        my_list.append(random.randrange(100000))
    return my_list

def pivot_fun(li,left,right):
    middle = int((left + right) / 2)
    if li[left]<li[right]:
        if li[middle]>li[right]:
            li[middle],li[right]=li[right],li[middle]
        elif li[middle]<li[left]:
            li[middle], li[left] = li[left], li[middle]
    else:
        li[left],li[right]=li[right],li[left]
        if li[middle]>li[right]:
            li[middle],li[right]=li[right],li[middle]
        elif li[middle]<li[left]:
            li[middle], li[left] = li[left], li[middle]
    li[middle],li[right ] = li[right ],li[middle]
    print(li)
    return right
# result = pivot_fun(my_list,0,len(my_list)-1)
# print(result)



def partition(li,left,right):
    piv = right
    i = left-1
    for j in range(left,right):
        if li[j]<=li[piv]:
            i +=1
            li[i], li[j] = li[j], li[i ]
    li[i + 1], li[piv] = li[piv], li[i + 1]
    return i+1

def main_quick_sort(li, left, right):
    # pivot = pivot_fun(li,left,right)
    if left<right:
        i = partition(li,left,right)
        main_quick_sort(li, left, i-1)
        main_quick_sort(li,i + 1,right)
    print(li)
list_ = generate_unsorted()
# result = main_quick_sort(list_, 0, len(list_) - 1)
# print(result)





mylist = [7,5,8,6,1,4,2,3,9,70]
def quick_sort(my_list,left,right):
    if left < right:
        i = partition(my_list, left, right)
        quick_sort(my_list, left, i - 1)
        quick_sort(my_list,i + 1,right)

        # print(my_list)
    return my_list
print(quick_sort(mylist, 0, len(mylist) - 1))








