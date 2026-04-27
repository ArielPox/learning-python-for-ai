import os
import time
from threading import get_native_id,Thread,RLock

# 定义speak函数每0.5秒说一次
class speakThread(Thread):
    def __init__(self,lock,**kwargs):
        super().__init__()
        self.lock=lock
        self.kwargs=kwargs
    def run(self):
        for i in range(10):
            with lock:
                print(f'说话的{i},进程pid是{os.getpid()},线程编号是{get_native_id()}')
            time.sleep(0.5)

# 定义一个学习函数零点五秒学一次
class studyThread(Thread):
    def __init__(self,lock,**kwargs):
        super().__init__()
        self.lock=lock
        self.kwargs=kwargs

    def run(self):
        for i in range(10):
            with lock:
                print(f'学习的{i},进程pid是{os.getpid()},线程编号是{get_native_id()}')
            time.sleep(0.5)

if __name__ == '__main__':
    print(f'start 主进程pid是{os.getpid()}，线程编号是{get_native_id()}')
    # 加线程锁:可以避免多个线程同时访问同一个资源
    lock=RLock()
    t1=speakThread(lock)
    t2=studyThread(lock)
    # 调用线程对象的start方法 会立即将线程交给操作系统进程调度
    t1.start()
    t2.start()
    # 让主进程等待线程t1,t2执行完毕
    t1.join()
    t2.join()
    print('this is the last row')

