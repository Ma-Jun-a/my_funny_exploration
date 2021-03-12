from itertools import chain

a = (2,3,4,5)
b= [4,44,222,3,2,3,23]
for x in chain(a,b):
    print(x)