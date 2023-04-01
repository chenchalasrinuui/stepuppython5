from threading import Thread,active_count

class MyThread(Thread):
    def __init__(self,id,name):
        Thread.__init__(self)
        self.thredId=id
        self.thredName=name

    def run(self):
        for v in range(10):
           print(self.thredName+' --->'+ str(v))


thread1= MyThread(1,'Thread1')
thread2= MyThread(2,'Thread2')

thread1.start()
thread2.start()
print(active_count())
print(thread1.is_alive())
print(thread1.name)

print(dir(thread1))




