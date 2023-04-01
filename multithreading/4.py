from threading import Thread,Lock
import time;

threadLock=Lock()
class Mythread(Thread):
    def __init__(self,name):
        super().__init__()
        #Thread.__init__()
        self.threadName=name

    def run(self):
        threadLock.acquire()
        self.transactions()
        threadLock.release()

    def transactions(self):
        for v in range(5):
            time.sleep(2)
            print(self.threadName,v)




t1=Mythread('Thread1')
t2=Mythread('Thread2')
t3=Mythread('Thread3')

t1.start()
t2.start()
t3.start()
