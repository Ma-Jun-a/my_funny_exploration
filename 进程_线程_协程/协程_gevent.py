import time
import greenlet
import gevent
from gevent import monkey

monkey.patch_all()#相当于把所有的time.sleep 换成gevent里面的有感知的sleep 对于编程者是无感知的
def task_a():
     for i in range(5):
        print('mission A is completing',i)
        time.sleep(0.5)


def task_b():
     for i in range(5):
         print('mission B is completing', i)
         time.sleep(0.5)

def task_c():
     for i in range(5):
         print('mission C is completing', i)
         time.sleep(0.5)

if __name__ == '__main__':
    g1 = gevent.spawn(task_a)
    g2 = gevent.spawn(task_b)
    g3 = gevent.spawn(task_c)
    g1.join()
    g2.join()
    g3.join()




