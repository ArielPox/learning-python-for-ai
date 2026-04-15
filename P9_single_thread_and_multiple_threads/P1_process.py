import os
import time
from multiprocessing import Process

# 定义speak函数每0.5秒说一次
def speak():
    for i in range(10):
        print(f'说话的{i},进程pid是{os.getpid()},父进程是{os.getppid()}')
        time.sleep(0.5)

# 定义一个学习函数零点五秒学一次
def study():
    for i in range(10):
        print(f'学习的{i},进程pid是{os.getpid()},父进程是{os.getppid()}')
        time.sleep(0.5)

# 1、当创建子进程的时候 python不会直接使用父进程中的函数 而是会启动一个全新的python解释器进程 重新执行当前的.py文件作为
# 在执行的过程中会重新定义一个speak函数 交给紫进程使用
# if __name__ == '__main__':根据上述描述 为了防止循环创建子进程 一定要使用if __name__ == '__main__':
if __name__ == '__main__':
    print('this is the first row')
    # 创建两个Process类的实例对象
    # tip1：P1与P2对应的是以后的两个子进程 在创建的之后就要指定进程的任务以及参数
    # tip2:P1与P2知识代码层面的两个进程对象，os并没有真正的创建两个进程
    p1=Process(target=speak)
    p2=Process(target=study)
    # 调用进程对象的start方法 会立即向操作系统申请一个进程 并且会将这个进程交给操作系统进行调度 这个过程是完全异步的 不会影响后面代码的执行
    p1.start()
    p2.start()
    print('this is the last row')

