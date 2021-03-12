from multiprocessing import Queue, Process


# q = Queue(3)
# q.put('A')# q.put('D',timeout=2) # q.put('E',timeout=2) # q.full()  q.empty()
# # q.get()# # q.get()# print(q.get())# q.put('B')# # q.put('C')
import time


def download(q):
    images = ['jpg.girl','women.jpg','you.jpg','ha.jpg','sm.jpg']
    for image in images:
        print('downloading {}'.format(image))
        time.sleep(0.5)
        q.put(image)

def open_file(q):
    while True:
        try:
            print('保存成功 {}'.format(q.get(timeout=3)))
        except:
            break

if __name__ == '__main__':
    q = Queue(3)
    p1 = Process(target=download,args=(q,))
    p2 = Process(target=open_file,args=(q,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print('下载完成')


