import os
import time
from multiprocessing import Process,current_process,Lock,RLock

# 进程之间不共享内存 所以变量是不共享的 但是lock是天然的跨进程的


def speak(lock):
    for i in range(10):
        # 加上的acquir可以继续运行，但是加锁的acquire()方法会阻塞，直到锁被释放，才能使用，acquire必须和release()方法配对使用
        lock.acquire()
        print(f'this is the speak process,{i}')
        lock.release()


def study(lock):
    for i in range(10):

        # with lock:会自动的完成两件事情，进入前自动执行lock.acquire()  退出之后自动执行lock.release()这样就算
        # 代码块中有异常的时候，也会自动执行lock.release()
        #Rlock可以多次使用 会计算上锁的次数
        with lock:
            print(f'this is the study process,{i}')
            time.sleep(0.5)


if __name__ == '__main__':
    print('this is the first row')
    # 在创建进程的时候需要传入一个lock对象
    lock=RLock()
    p1=Process(target=speak,args=(lock,))
    p2=Process(target=study,args=(lock,))
    p1.start()
    p2.start()
    print('this is the last row')

