import os
import time
from concurrent.futures import ProcessPoolExecutor

from pydantic.v1.datetime_parse import parse_time


# 1创建进程池执行器 使用submit方法 只提交不阻塞 使用shutdown方法阻塞等待
def work(n):
    print(f'{os.getpid()}进程开始执行任务{n}')
    time.sleep(1)
    return f'this is 进程{os.getpid()}任务{n}执行完毕'

if __name__ == '__main__':
    executor = ProcessPoolExecutor(max_workers=3)
    futures=[executor.submit(work,i) for i in range(10)]
    # 阻塞主进程 等待进程池中所有任务执行完毕
    executor.shutdown(wait=True)
    # 返回的结果任务return回的结果
    for i in futures:
        print(i.result())
    print('所有任务执行完毕')
