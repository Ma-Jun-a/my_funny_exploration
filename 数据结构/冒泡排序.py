import random
my_list = []
for i in range(1000):
    my_list.append(random.randrange(100000))
list_ = my_list

def judge(x,y):
    if x < y:
        x, y = x, y
        return  x, y
    else:
        x, y = y, x
        return  x, y

def sort(list):
    for n in range(1000):
        for i in range (999-n):
            list[i],list[i+1] = judge(list[i],list[i+1])
    return list
print(sort(list_))