import threading
import time
 
exitFlag = 0
threads = {}
 
class myThread (threading.Thread):   #继承父类threading.Thread
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):                   #把要执行的代码写到run函数里面 线程在创建后会直接运行run函数 
        if(self.name == "Thread-1"):
            print(self.name)
            threads['thread-2'].prints()
        print("Starting " + self.name)
        print_time(self.name, self.counter, 5)
        print("Exiting " + self.name)
    def prints(self):
        print(self.name + " has been call")
 
def print_time(threadName, delay, counter):
    while counter:
        if exitFlag:
            (threading.Thread).exit()
        time.sleep(delay)
        print("%s: %s" % (threadName, time.ctime(time.time())))
        counter -= 1
 
# 创建新线程
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)

threads['thread-1'] = thread1
threads['thread-2'] = thread2
 
# 开启线程
thread1.start()
thread2.start()
 
print("Exiting Main Thread")