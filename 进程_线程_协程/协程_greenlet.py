import time
import greenlet

def task_a():
     for i in range(5):
        print('mission A is completing',i)
        g2.switch()
        time.sleep(0.5)


def task_b():
     for i in range(5):
         print('mission B is completing', i)
         g3.switch()
         time.sleep(0.5)


def task_c():
     for i in range(5):
         print('mission C is completing', i)
         g1.switch()
         time.sleep(0.5)

if __name__ == '__main__':
    g1 = greenlet.greenlet(task_a)
    g2 = greenlet.greenlet(task_b)
    g3 = greenlet.greenlet(task_c)

    g1.switch()


