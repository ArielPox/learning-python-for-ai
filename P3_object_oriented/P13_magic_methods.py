# Python 的魔法方法是类中__xxx__格式的内置方法，由解释器自动触发，
# 让自定义类支持 Python 原生语法和特性，是实现面向对象核心功能的底层基础。
# python在打印实例对象时候 会将其转化为字符串，打印的时候会自动的调用instance.__str__() 最终方法在Object父类上找到 打印的是对象的地址

class Person:
    # 函数在类中称之为方法 _init_ 是特殊方法，在创建对象时调用 主要是给当前正在创建的实例对象添加属性
    # _init_方法接受到的参数是当前正在创建的实例对象，self
    planet='moon'
    max_age=100
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    # python中打印的时候会调用str
    def __str__(self):
        return f"{self.name}-{self.age}-{self.gender}"

    # __len__调用对象的时候
    def __len__(self):
        return len(self.__dict__)

    # 对象的1<小于对象2就会调用
    def __lt__(self,other):
        return self.age<other.age

    # 对象1大于对象2
    def __gt__(self, other):
        return self.age>other.age

    def __eq__(self,other):
        return self.__dict__==other.__dict__
    # 当访问不存在的属性的时候就会调用getattr
    def __getattr__(self, item):
        print(f"访问的{item}属性不存在")

P1=Person('andy','10','women')
P2=Person('lili','19','men')
P3=Person('lili','19','men')

print(P1)
print(P2)
print(P1>P2)
print(P1<P2)
print(P1==P2)
print(P2==P3)
print(P3.address)
