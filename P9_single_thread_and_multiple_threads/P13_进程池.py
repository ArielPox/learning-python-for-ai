import os
import time
from concurrent.futures import ProcessPoolExecutor

# 1创建进程池执行器 使用submit方法 只提交不阻塞 使用shutdown方法阻塞等待
def work(n):
    print(f'{os.getpid()}进程开始执行任务{n}')
    time.sleep(1)

if __name__ == '__main__':
    with ProcessPoolExecutor(max_workers=3) as executor:
        for i in range(10):
            executor.submit(work,i)
        executor.shutdown(wait=True)
    print('所有任务执行完毕')
