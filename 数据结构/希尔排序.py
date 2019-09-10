import random
import time

my_list = []
for i in range(1000):
    my_list.append(random.randrange(100000))
list_ = my_list
def xier_sort(list,n):
    for x in range(1,1000,n):
        i = x
        while i > 0:
            if list[i] < list[i-n]:
                list[i-n],list[i] = list[i],list[i-n]
            else:
                list[i] = list[i]
            i -= 1
    t_list = list
    return t_list
# print(xier_sort(list_,1))

def evaluation(func,*args):
    start = time.clock()
    list = args[0]
    n = args[1]
    func(list,n)
    return time.clock() - start
print(evaluation(xier_sort,list_,1))



