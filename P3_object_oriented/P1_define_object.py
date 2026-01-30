# 定义类使用大驼峰写法
class Person:
    # 函数在类中称之为方法 _init_ 是特殊方法，在创建对象时调用 主要是给当前正在创建的实例对象添加属性
    # _init_方法接受到的参数是当前正在创建的实例对象，self
    def __init__(self,name,age):
        self.name=name
        self.age=age

P1=Person('andy',18)
# 可以使用点语法将获得实例对象的属性
print(P1.name)

# 通过_dict_可以查看实例对象身上全部的属性 可以直接使用点语法添加属性
print(P1.__dict__)
# 实例对象通过点语法添加属性，称之为实例属性 与类属性还有其他的实例对象互相隔离
P1.address='beijing'
print(P1.__dict__)
# 可以通过type函数查看当前的实例对象是由哪一个类创建的
print(type(P1))