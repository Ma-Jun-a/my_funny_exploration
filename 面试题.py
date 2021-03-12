import random
# 要求输出是里表中其中三个数的积 例如【84 = 7*3*4】
my_list = [1,7,3,4]

def function(li):
    you_list = []
    list_ = li[:]
    y = 1
    for i in range(len(li)):

        list_[i]=1
        for x in list_:
            y = y*x
        list_[i] = li[i]
        you_list.append(y)
        y = 1
    return you_list
result = function(my_list)
print(result)





