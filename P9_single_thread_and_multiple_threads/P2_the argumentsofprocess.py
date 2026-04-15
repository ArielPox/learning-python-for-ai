import os
import time
from multiprocessing import Process,current_process

# 定义speak函数每0.5秒说一次
def speak(a,b,msg):
    print(f'进程名称是{current_process().name},位置参数是{a,b},关键字参数是{msg}')
    for i in range(10):
        print(f'说话的{i},进程pid是{os.getpid()},父进程是{os.getppid()}')
        time.sleep(0.5)

# 定义一个学习函数零点五秒学一次
def study():
    print(f'进程名称是{current_process().name}')
    for i in range(10):
        print(f'学习的{i},进程pid是{os.getpid()},父进程是{os.getppid()}')
        time.sleep(0.5)

# 1、当创建子进程的时候 python不会直接使用父进程中的函数 而是会启动一个全新的python解释器进程 重新执行当前的.py文件作为
# 在执行的过程中会重新定义一个speak函数 交给紫进程使用
# if __name__ == '__main__':根据上述描述 为了防止循环创建子进程 一定要使用if __name__ == '__main__':
if __name__ == '__main__':
    print('this is the first row')
    # process可以传递的参数：group 默认是None
    # target 子进程要执行的可调用对象默认是None
    # args给target传递的位置参数 使用元组
    # kwargs给target传递的关键字参数 使用字典
    # daemon 给子进程设置一个守护进程 默认是False
    # name 给进程设置一个名称 默认是Process-1

    p1=Process(target=speak,args=(1,2),kwargs={'msg':'hello world'})
    p2=Process(target=study,name='study process')
    # 调用进程对象的start方法 会立即向操作系统申请一个进程 并且会将这个进程交给操作系统进行调度 这个过程是完全异步的 不会影响后面代码的执行
    p1.start()
    p2.start()
    print('this is the last row')

