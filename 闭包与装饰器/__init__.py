import time
from functools import wraps

def timetise(fun):
    print(fun.__str__())
    @wraps(fun)
    def wrapper(*args,**kwargs):
        start = time.time()
        result = fun(*args,**kwargs)
        end = time.time()
        print(fun.__name__,end-start)
        return result
    return wrapper

@timetise
def tessttt(num):
    re = 0
    for i in range(num):
        time.sleep(0.001)
        i+=i*1.06
        re = i
        # print(i)

    print('done',re)
    return re

tessttt(5000)

