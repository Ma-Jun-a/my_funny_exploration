import threading
import time


list_ = [0]*10
lock = threading.Lock()
def task1():
    lock.acquire()
    for i in range(len(list_)):
        list_[i] = 1
        print('task1执行结束：', i)
        i += 1
    lock.release()
def task2():
    lock.acquire()
    for i in range(len(list_)):
        print('task2执行结束：',list_[i])
        time.sleep(0.5)
    lock.release()

if __name__ == '__main__':
    t1 = threading.Thread(target=task1,daemon=True)
    t2 = threading.Thread(target=task2,daemon=True)
    t1.start()
    t2.start()
    t1.join()
    t2.join()


    print('主进程结束')
