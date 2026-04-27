

import os
import time
from concurrent.futures import ProcessPoolExecutor,as_completed
from multiprocessing import Process
from wsgiref.util import request_uri


def work(n):
    print(f'{os.getpid()}进程开始执行任务{n}')
    time.sleep(1)
    return f'this is 进程{os.getpid()}任务{n}执行完毕'

def done_callback(future):
    print(f'任务完成',future.result())

# #region
# if __name__ == '__main__':
#     executor = ProcessPoolExecutor(max_workers=3)
#     result_list=[]
#     # 生成器是阻塞的
#     results=executor.map(work,range(10))
#     # 获取results生成器的内容
#     print(list(results))
#     # 等待所有任务完成
#     executor.shutdown(wait=True)
#     print('所有任务执行完毕')
# #endregion

# 进程池使用with 程序是
if __name__ == '__main__':
    with ProcessPoolExecutor(max_workers=3) as executor:
        results=executor.map(work,range(10))
        # 阻塞主进程 等待进程池中所有任务执行完毕
        executor.shutdown(wait=True)
        # 获取结果
        print(list(results))
    print('所有任务执行完毕')