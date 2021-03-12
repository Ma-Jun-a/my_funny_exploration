import queue
import threading
import time
#死锁 设立 timeout
queue.LifoQueue()#后入先出
queue.PriorityQueue()#优先级队列
def produce(q):
    print('生产者开始生产---')
    for i in range(9):
        q.put(i)
        print('正在生产', i)
        time.sleep(1)

    q.put(None)
    q.task_done()

def consumer(q):
    print('消费者开始消费')
    while True:
        item = q.get()
        if item is None:
            break
        print('正在消费', item,tp.name)
        time.sleep(4)

    q.task_done()

if __name__ == '__main__':
    q = queue.Queue(5)
    # arr =[]
    tp = threading.Thread(target=produce,args=(q,))

    tc = threading.Thread(target=consumer,args=(q,))
    tp.start()
    tc.start()
    tp.join()
    tc.join()
    print('END')




