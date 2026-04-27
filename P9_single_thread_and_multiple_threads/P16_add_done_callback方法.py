# 在Python 多线程里，call_done_back 是线程任务执行完毕后，自动调用回调函数通知结果的标准写法，专门用来解决：
# 线程跑完不知道怎么通知主线程
# 子线程结果无法安全返回
# 多任务完成后统一收尾

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
if __name__ == '__main__':
    executor = ProcessPoolExecutor(max_workers=3)
    result_list=[]
    # 开启7个任务 指定回调函数
    for i in range(8):
        f=executor.submit(work,i)
        f.add_done_callback(done_callback)
    # 所有的任务都完成
    print(request_list)