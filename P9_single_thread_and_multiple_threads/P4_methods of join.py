import os
import time
from multiprocessing import Process

# join的使用：阻塞当前的京城，等join之前的进程执行完毕之后再继续执行
# join(timeout) 表示等待多节s之后再继续执行
# p.join（）是让执行这行代码的进程等待这个进程p 当时间到达之后 进程并没有终止，只是不再等待。join必须在start方法之后执行
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


if __name__ == '__main__':
    print('this is the first row')
    # 创建两个Process类的实例对象
    p1=Process(target=speak)
    p2=Process(target=study)
    p1.start()
    # 主进程会等待p1 5S
    p1.join(3)
    p2.start()
    print('this is the last row')

