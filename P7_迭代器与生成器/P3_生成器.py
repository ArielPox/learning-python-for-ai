# 1.生成器:
# 生成器函数:函数中出现yield关键字,就是生成器函数
# 生成器对象:生成器函数调用之后,函数的不会立即执行,而是返回的是生成器对象,生成器对象可以调用next()方法,也可以使用for循环迭代
# 不管函数能不能执行到yield位置 只要有yield就是生成器函数

# 2.写在生成器函数的代码,需要通过生成器对象来执行
# 1.调用生成器对象的__next__ 方法 会让生成器函数中的代码开始执行
# 2.当生成器函数中的代码执行到yield位置时,会返回yield后面的值,并暂停当前函数的执行
# 3.当生成器对象再次调用__next__ 方法时,会继续从上次暂停的位置继续执行
# 4.当生成器函数中的代码执行到yield位置时,会返回yield后面的值,并暂停当前函数的执行
# 5.当生成器函数中的代码执行到return位置时,会返回return后面的值,并结束当前函数的执行
# 6.当生成器对象再次调用__next__ 方法时,会抛出StopIteration异常,表示生成器对象已经迭代完毕
# yield后面的写的表达式 会作为本次__next__方法返回的值

# 生成器对象是一种特殊的迭代器，通过yield自动实现了迭代器协议
#region
def demo():
    print('demo begin')
    print(100)
    yield 'this is the first yield'
    print('200')
    yield 'this is the second yield'
    print('300')
    return 'this is the return'

# iterate the generator
d=demo()
# for i in d:
#     print(i)

print('遍历的背后的逻辑')
gen=iter(d)
while True:
    try:
        value=next(gen)
        print(value)
    except StopIteration:
        break
#endregion

# yield也可以在for中使用
#region
def create_car(total):
    for i in range(total):
        yield f'this is the car {i+1}'

cars=create_car(5)
while True:
    try:
        car=next(cars)
        print(car)
    except StopIteration:
        break
#endregion

# yield from 可以将函数中的迭代对象一次迭代出去
#region
def demo1():
    nums=[1,2,3,4,5]
    yield from nums
d1=demo1()
while True:
    try:
        value=next(d1)
        print(value)
    except StopIteration:
        break
#endregion

# 生成器.send(value)可以让函数继续执行的同时给上一次yield 传值生成器执行到 yield 表达式 时会暂停，send() 发送的值会赋值给这个 yield 表达式
# 第一次必须用 next() 或 send(None) 启动生成器（不能直接传有效值，否则报错）
# next(生成器)：只恢复生成器执行，不传递值，返回生成器的 yield 结果
# 生成器.send(值)：恢复生成器执行 + 向生成器内部传值，同时返回 yield 结果
#region
def demo2():
    print('generator launch')
    value=yield 'this is the first yield'
    print(f'this is the value from outside：{ value}')
    yield value*2
gen=demo2()
next(gen)
result=gen.send(100)
print(f'the result of demo2 that accept 100 is {result}')
#endregion

