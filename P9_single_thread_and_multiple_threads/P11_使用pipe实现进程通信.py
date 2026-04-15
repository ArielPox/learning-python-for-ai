import time
from multiprocessing import Process,Pipe

def test1(con1):
    time.sleep(1)
    con1.send(100)
    print(f'test1发送了数据100')

def test2(con2):
    time.sleep(1)
    print(f'test2接收到数据{con2.recv()}')

if __name__ == '__main__':
    # 创建管道
    con1,con2=Pipe()
    # 创建进程
    p1=Process(target=test1,args=(con1,))
    p2=Process(target=test2,args=(con2,))
    # 启动进程
    p1.start()
    p2.start()