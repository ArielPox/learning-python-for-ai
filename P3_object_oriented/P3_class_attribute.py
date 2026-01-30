# 实例对象通过点语法增加的属性为实例化属性
class Person:
    # 类属性作为公共属性，可以被类访问到 也可以被实例对象访问到
    species='animal',
    max_age=1000
    # 函数在类中称之为方法 _init_ 是特殊方法，在创建对象时调用 主要是给当前正在创建的实例对象添加属性
    # _init_方法接受到的参数是当前正在创建的实例对象，self
    def __init__(self,name,age):
        self.name=name
        if(age>=Person.max_age):
            print('exceed the max age')
        else:
            self.age=age

P1=Person('andy',18)
print(Person.__dict__)
print(P1.species)
print("实例对象添加的属性与方法与类的同名就会被覆盖，实例兑现调用属性与方法都是先从自身找 没有就从构造的类身上找")
P1.species='human'
print(P1.__dict__)
P2=Person('tom',1001)