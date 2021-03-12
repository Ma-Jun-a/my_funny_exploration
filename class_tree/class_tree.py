# def class_tree(cls,indent):
#     print('.' * indent +cls.__name__)
#     for supercls in cls.__bases__:
#     # if supercls == cls.__bases__:
#     #     print(cls.__bases__)
#         class_tree(supercls,indent+3)
#
# def instance_tree(inst):
#     print('tree of %s' % inst)
#     class_tree(inst.__class__, 3)
#
# def self_test():
    # class A: pass
    # class B(A):pass
    # class C(B):pass
    # class D(C): pass
    # class E: pass
    # class F(D,E): pass

    # class_dict = []
    # class_dict.append()
    # instance_tree(class_dict[0])
    # instance_tree(B())
    # instance_tree(F())
from collections import deque, MutableSequence


class Self_Test(object):

    def __init__(self):
        self.inst_dict = []

    def append_instance(self,inst):
        # if self.inst_dict[0] is None:
        self.inst_dict.append(inst)
        # else:
        #     pass

    def class_tree(self,cls, indent):
        print('.' * indent +cls.__name__)
        for supercls in cls.__bases__:
            # if supercls == cls.__bases__:
            #     print(cls.__bases__)
            self.class_tree(supercls,indent+3)

    def instance_tree(self):
        inst = self.inst_dict[0]
        print('tree of %s' % inst)
        self.class_tree(inst.__class__, 3)

# test = Self_Test()
# from flask import Flask
#
# app = Flask('app')
# from celery import Celery
# celery = Celery('celery_task')
# deqcue = deque()
# Mquence= MutableSequence()
# class A(object):
#     pass
# class B(A):
#     pass
# class C(B):
#     pass
# class F(Flask):
#     pass
# class D(C,F):
#     pass

# d = D('sd')
# test.append_instance(deqcue)
# test.instance_tree()
i = 0
j= 0
while  i < 100:
    i+=1
while  j < 100:
    j+=1
print(i,j)






# if __name__ == '__main__':
# self_test()




