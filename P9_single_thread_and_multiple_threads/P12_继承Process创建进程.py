from multiprocessing import Process,current_process
import os,time


class MyProcess(Process):
    def __init__(self,name):
        super().__init__()
        self.name=name
    def run(self):
        print('%s is running'%self.name)
        time.sleep(2)
        print('%s is done'%self.name)
        print('进程id是：',os.getpid())
        print('父进程id是：',os.getppid())
        print('进程名称是：',current_process().name)
        print('进程pid是：',current_process().pid)

if __name__ == '__main__':
    p=MyProcess('子进程')
    p.start()
    print('主进程结束')