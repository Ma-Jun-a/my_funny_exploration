import random
import time模块

my_list = []
for i in range(5000):
    # my_list.append(random.randrange(10000))
    my_list.append(i)
list_ = my_list

def judge(x,y):
    global flag
    flag = 0
    if x < y:
        x, y = x, y
        flag = 0
        return  x, y,flag
    else:
        x, y = y, x
        flag = 1
        return  x, y,flag

def sort(list,len):
    start = time模块.clock()
    for n in range(len):
        flag2 = 0
        for i in range ((len-1)-n):
            list[i],list[i+1],flag = judge(list[i],list[i+1])
            if flag == 1:
                flag2 = 1
        if flag2 == 0:
            end = time模块.clock()
            return "有测试的time: ",end-start
    # end = time.clock()
    # return list,"time: ",end-start
print(sort(list_,5000))


def sort2(list,len):
    start = time模块.clock()
    for n in range(len):

        for i in range ((len-1)-n):
            list[i],list[i+1],flag= judge(list[i],list[i+1])

    end = time模块.clock()
    return "没有flag的测试time: ",end-start

print(sort2(list_,5000))





























# class My_Test(object):
    # @staticmethod
    # def zhunbei():
    #     import random
    #     my_list=[]
    #     for i in range(1000):
    #         my_list.append(random.randrange(100000))
    #     return my_list
    # list_ = zhunbei()
    # def __init__(self,func_name):
    #     self.func_name = func_name
    # def tes_func(self):
    #     self.func_name(self.list_)
# t1 = My_Test(sort)
# t1.tes_func()
