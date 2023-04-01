from threading import Thread
import time
#print(type(Thread))
#print(dir(Thread))

def f1():
    for v in range(10):
        time.sleep(2)
        print('f1---> t1 --->'+ str(v))



def f2():
    for v in range(10):
        print('f2---> t2 --->'+ str(v))

class T:
    def f3(self):
        for v in range(10):
            print('f3---> t3 --->'+ str(v))


t1=Thread(target=f1)
t2=Thread(target=f2)
t3=Thread(target=T().f3)

t1.start()
t1.join()
t2.start()
t2.join()
t3.start()




