import os
from multiprocessing.pool import Pool

from random import random
import time

# 什么时候回调全部执行完毕后回调
def task(name):
    print('start mission {}'.format(name))
    start = time.time()
    time.sleep(random())
    end = time.time()
    print('mission accomplished {}, time cost:{}'.format(name,(end-start)),os.getpid())
    # return 'mission accomplished {}, time cost:{}'.format(name,(end-start)),os.getpid()
container = []
def callback_func(content):

    container.append(content)
    return container
if __name__ == '__main__':
    pool = Pool(3)

    tasks = ['刷牙','洗脸','吃早饭','喝水','上班','下班','睡觉']
    for task1 in tasks:
        pool.apply_async(task,args=(task1,),callback=callback_func)
    pool.close()
    pool.join()
    # for c in container:
    #     print(c)
    print('tasks over! 好处是可以重复利用创建好的进程，进程的开销太大')