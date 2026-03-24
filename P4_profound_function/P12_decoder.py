# 在不改变原函数情况下面 给函数加一点功能，装饰器本质是一个 “接收函数、返回新函数” 的函数，咱们写一个 “加前后动作” 的装饰器
# 1.函数装饰器
# 定义装饰器
def decfunc(func):
    # 定义新函数加上额外的的 前后动作
    def morefnc():
        print("front action")
        func()
        print("back action")
    return morefnc()

# 给目标函数加上装饰器
@decfunc
def func2():
    print("I am a normal function")

# 带参数的函数装饰器 只需要使用*args **kwargs 就可以传入参数的
# 定义装饰
def decofunc2(func):
    def morefunc2(*args, **kwargs):
        print(f'打开冰箱')
        result= func (*args,**kwargs)
        print(f'关上冰箱')
        return result
    return morefunc2

# 加上装饰器
@decofunc2
def func3(a,key: str):
    print(f'打开{a}的{key}')
    return 'end'
func3('a','b')
