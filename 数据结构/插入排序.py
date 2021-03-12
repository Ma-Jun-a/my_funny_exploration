import random
my_list = []
for i in range(1000):
    my_list.append(random.randrange(100000))
list_ = my_list
# print(list_)
def insert_sort(list):
    sorted_list = list
    for x in range(2,1000):
        i = x
        while i>0 :
            if sorted_list[i] < sorted_list[i - 1]:
                sorted_list[i],sorted_list[i-1] = sorted_list[i-1],sorted_list[i]
            else:
                sorted_list[i] = sorted_list[i]
            i -= 1
    return sorted_list
print(insert_sort(list_))

from collections import deque
from queue import Queue
import heapq
a = Queue(maxsize=5)
a.put(3)
a.put(2)
a.put(1,block=True,timeout=3)


