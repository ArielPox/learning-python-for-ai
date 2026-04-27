# 1.coroutine function 协程函数 使用async修饰的函数 就是协程函数
# 2.协程对象从routine object调用协同函数 得到协同对象
import asyncio


async def work(n):
    print(f'开始执行任务{n}')
    await asyncio.sleep(1)
    print(f'任务{n}执行完毕')
    return f'this is 协程任务{n}执行完毕'

# 调用协程函数就会得到协程对象
coroutine_obj=work(1)

#asyncio.run 函数会自动创建一个事件循环，将接收到的协程对象 包装为一个任务的 交给事件循环 启动事件循环
result=asyncio.run(coroutine_obj)
print(result)