# 抽象类是面向对象编程（OOP）中的特殊类，无法被直接实例化（不能创建对象），
# 主要作用是定义子类的通用规范与通用行为，强制子类实现其中的抽象方法，实现代码复用和接口约束
from abc import ABC,abstractmethod

# MustRun继承ABC之后就是抽象类
class MustRun(ABC):
    # MustRun的子类必须要实现run这个方法
    @abstractmethod
    def run(self):
        pass

class Person(MustRun):
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def run(self):
        print('this is a abstract class methods')

    def comm_meth(self):
        print('common method can be definited in abstract class')

P1=Person('andy',10)
Person.comm_meth(P1)
P1.run()