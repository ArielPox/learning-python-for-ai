# 类装饰器：
# 1.包含__call__方法的类，当类实例化对象时，会自动调用__call__方法
# 2.__call__方法接受一个函数作为参数 返回新的函数

class SayHi:
    def __call__(self,func):
        def inner(*args,**kwargs):
            print('this is class decoder')
            return func(*args,**kwargs)
        return inner

@SayHi()
def add(a,b):
    print(f'the result is {a+b}')

# 使用SayHi去装饰add函数
add(1,2)

# 2.带参数的类装饰器
class SayHi1:
    def __init__(self,name):
        self.name=name
    def __call__(self,func):
        def inner(*args,**kwargs):
            print(f'this is {self.name} class decoder')
            return func(*args,**kwargs)
        return inner

@SayHi1('SayHi1')
def add(a,b):
    print(f'the result is {a+b}')

add(1,10000)


# 3.多层装饰器
class SayHi2:
    def __init__(self,name):
        self.name=name
    def __call__(self,func):
        def inner(*args,**kwargs):
            print(f'this is {self.name} class decoder')
            return func(*args,**kwargs)
        return inner

class SayHi3:
    def __init__(self,name):
        self.name=name
    def __call__(self,func):
        def inner(*args,**kwargs):
            print(f'this is {self.name} class decoder')
            return func(*args,**kwargs)
        return inner

@SayHi2('SayHi2')
@SayHi3('SayHi3')
def add(a,b):
    print(f'the result is {a+b}')

add(1,2000)