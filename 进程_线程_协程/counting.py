import time
from threading import Thread


class Counting(object):
    def __init__(self):

        self._running = True
    def terminate(self):
        self._running = False
    def run(self,t):
        while self._running and t>0:
            print('T-minus', t)
            t -= 1
            time.sleep(5)
c = Counting()
t = Thread(target=c.run, args=(10,))
t.start()
c.terminate()
t.join() 