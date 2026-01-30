from datetime import datetime
class Person:
    # 函数在类中称之为方法 _init_ 是特殊方法，在创建对象时调用 主要是给当前正在创建的实例对象添加属性
    # _init_方法接受到的参数是当前正在创建的实例对象，self
    planet='moon'
    max_age=100
    def __init__(self,name,age):
        self.name=name
        self.age=age

    # 使用@static methods修饰的方法为类的静态方法得到，静态方法只单纯的定义在类中
    # 内部没有接受到self于cls参数，不会访问类和实例相关的内容
    # 常用于定义于类相关的工具方法，可以被类调用，也可以被实例调用 但是不推荐
    @staticmethod
    def is_adult(year):
        cur_year=datetime.now().year
        # 计算年纪
        age=cur_year-year
        return age>=18

    @staticmethod
    def mask_idcard(idcard):
        return idcard[:4]+'******'+idcard[-4:]

P1=Person('andy',18)
print(P1.is_adult(2009))
print(Person.is_adult(1990))
print(Person.mask_idcard('110101199012345678'))
print(Person.__dict__)