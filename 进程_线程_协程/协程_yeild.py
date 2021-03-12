import time


def task_a():
     for i in range(5):
        print('mission A is completing',i)
        yield
        task_b()
        time.sleep(0.5)


def task_b():
     for i in range(5):
         print('mission B is completing', i)
         yield
         task_c()
         time.sleep(0.5)


def task_c():
     for i in range(5):
         print('mission C is completing', i)
         yield
         task_a()
         time.sleep(0.5)

if __name__ == '__main__':
    g1 = task_a()
    g2 = task_b()
    g3 = task_c()

    while True:
        try:
            next(g1)
            next(g2)
            next(g3)
        except:
            break


