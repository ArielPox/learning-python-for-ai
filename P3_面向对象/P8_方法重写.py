class Person:
    # 函数在类中称之为方法 _init_ 是特殊方法，在创建对象时调用 主要是给当前正在创建的实例对象添加属性
    # _init_方法接受到的参数是当前正在创建的实例对象，self
    planet='moon'
    max_age=100
    def __init__(self,name,age):
        self.name=name
        self.age=age

    # 在类里面定义的函数作为方法可以被所有的实例对象调用 这些方法称之为实例方法
    def show(self,msg):
        print(f"show the {msg}")