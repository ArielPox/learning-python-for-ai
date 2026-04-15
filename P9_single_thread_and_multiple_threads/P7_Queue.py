from multiprocessing import Queue

from numpy.matlib import empty

# 创建队列 不限制大小
q=Queue()

# 创建队列 限制大小 最多保存10个元素
q1=Queue(3)

# put方法：添加元素
q1.put('hello world')
q1.put(10)
q1.put(10.5)

# get方法 获取元素
# q.get() 获取队列中的元素，如果队列为空，则阻塞
# print(q1.get())
# print(q1.get())
# print(q1.get())
# print(q.get())

# empty()判断队列是不是空
print(q1.empty())

# full判断队列是不是满
print(q1.full())

# qsize可以得到长度
print(q1.qsize())

# 队列有等待模式
# 1.队列满的时候 继续put就会进入等待模式，等待别人调用get
# 2.队列空的时候 继续get就会进入等待模式，等待别人调用put
# 3.队列已经满可以put(元素，阻塞时间)就会等待指定的时间
# 4.put_nowait方法：直接给队列中加元素 不会进入等待模式，如果队列已经满了，就会抛出异常 等价于put(元素，block=False)
# 5.get(timeout): 从队列中获取元素，如果队列为空，则等待指定的时间
# 6.get_nowait(): 从队列中获取元素，如果队列为空，则直接抛出异常 等价于get(block=False)

# 多进程演示 队列满之后 再次put会等待
if __name__ == '__main__':
    # 创建一个队列
    q=Queue(2)
    q.put('data1')
    q.put('data2')
    print(f'判断队列是否满：{q.full()}')

    # 创建子进程p
    p=Process(target=test,args=(q,))
    # 开启子进程 3S之后从中取出一个元素
    p.start()

    print('向满队列中加一个元素')
    q.put('data3')

    print('目前队列中的元素有：')
    print(q.get())
    print(q.get())