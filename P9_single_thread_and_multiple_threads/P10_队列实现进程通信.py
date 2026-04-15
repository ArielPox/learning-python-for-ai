import time
from multiprocessing import Process,Queue

def test1(q):
    for i in range(10):
        print(f'test1放入数据,{i}')
        time.sleep(0.5)
        q.put(i)

def test2(q):
    for i in range(10):
        print(f'test2取出数据,{q.get()}')
        time.sleep(0.5)

# 进程通信
if __name__ == '__main__':
    q=Queue(10)
    p1=Process(target=test1,args=(q,))
    p2=Process(target=test2,args=(q,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print('主进程结束')