# 异步：遇见等待就会让出CPU
# 协程：遇IO 阻塞时让出CPU，让事件循环去执行其他协程。
# 协程: 单线程实现多任务



# await
# 写在async函数内部，用来暂停当前协程。
# 遇到 IO 阻塞时让出 CPU，让事件循环去执行其他协程。
# IO 完成后再恢复当前代码继续运行，是协程实现并发的关键。
# 协程
# 轻量级并发，运行在单线程中，由程序自身调度，开销极小。
# 依靠async定义、await切换任务。
# 适合IO 密集型：网络请求、数据库、读写文件。
# 不适合大量 CPU 计算，无法利用多核。
# 对比：进程管计算、线程管普通 IO、协程管高并发 IO。

import asyncio
import time


# define a asyn function
async def work(num,time):
    await asyncio.sleep(time)
    print(f'开始执行任务{num}.....')
    # mimic IO await
    await asyncio.sleep(time)
    return f'任务{num}执行完毕'

async def main():
    print('begin')
    start=time.time()
    # asyncio.create_task(work(1,2),,,,)创建一个可以被事件循环运行的任务
    conti1=asyncio.create_task(work(1,2))
    conti2=asyncio.create_task(work(2,2))
    conti3=asyncio.create_task(work(3,1))

    # 等待conti1完成
    res1=await conti1
    print(res1)
    # 等待conti3 完成
    res2=await conti2
    print(res2)
    # 等待conti3 完成
    res3=await conti3
    print(res3)

    print(f'所有任务执行完毕，耗时{time.time()-start}')
    return 'end of main'

# 将携程对象交给事件循环
result=asyncio.run(main())
print(result)