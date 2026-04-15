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


if __name__ == '__main__':
    print('this is the first row')

    p1=Process(target=speak)
    p2=Process(target=study)
    p1.start()
    p2.start()
    time.sleep(3)
    print('即将终止study进程，terminate不会引起finally的运行')
    p2.terminate()
    print('this is the last row')

# terminate() = 操作系统级强制终止
# 它不是 Python 层面的优雅停止，而是直接告诉操作系统：
# 立刻回收这个线程 / 进程的资源，停止运行。
# 结果就是：
# 线程当前执行的代码瞬间中断
# finally 块完全没有机会被执行
# 所有清理逻辑（关闭文件、释放锁、断开连接、打印日志）全部失效
# finally 的执行前提
# Python 中 finally 只有在正常退出 try 块时才会执行：
# return
# 抛出异常被捕获
# 代码执行完毕
# 暴力终止不属于正常退出，所以 finally 直接跳过。

