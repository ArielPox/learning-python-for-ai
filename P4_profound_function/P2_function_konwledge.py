# 1.函数也是对象
from aiohttp.log import web_logger

a1=10 #int类的实例对象
a2='hello'# str class`s instance
a3=[1,2,3] # list class`s instance

# function class`s instance
def welcome():
    print('hi')

print(type(a1))
print(type(a2))
print(type(a3))
print(type(welcome()))

# 2. 函数可以动态的添加属性赋值
def welcome2():
    print('hi')
welcome2.say='say hi'
welcome2.version='v1'
say_hi=welcome2
say_hi()
print(welcome2.say)
print(welcome2.version)

# 3.函数传入不可变参数不会影响外部参数，函数传入可变参数 函数内部改变可变参数 外部一样被改变
# 不可变参数
def fun1(data):
    print('before change data',data,id(data))
    data=999
    print('after change data',data,id(data))
a=88
print('before use fun1',a,id(a))
fun1(a)
print('after use fun1',a,id(a))

# 可变参数
def fun1(data):
    print('before change data',data,id(data))
    data[2]=999
    print('after change data',data,id(data))
b=[1,2,3]
print('before use fun1',b,id(b))
fun1(b)
print('after use fun1',b,id(b))

# 4.函数也可以作为参数
def fun3():
    print('fun3 say hi')

def fun4(f):
    print('use func4')
    f()
fun4(fun3)

# 5.函数可以作为返回量返回
def welcome3():
    greeting = '你好啊'  # 外部函数的变量
    def show_msg(msg):
        print(greeting, msg)  # 引用外部变量
    return show_msg

say_hi = welcome3()
# 第二步：用接收的函数传参执行，即可调用内部的show_msg
say_hi('小明')   # 输出：你好啊 小明
say_hi('编程新手') # 输出：你好啊 编程新手
say_hi('闭包')   # 输出：你好啊 闭包

