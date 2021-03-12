import threading
import time

storage = threading.local()
storage.foo = 1

class Another_thread(threading.Thread):
    def run(self):
        storage.foo = 2
        # time.sleep(1)
        print(storage.foo)
if __name__ == '__main__':

    another = Another_thread()
    another.start()

    time.sleep(0.5)
    print(storage.foo)



