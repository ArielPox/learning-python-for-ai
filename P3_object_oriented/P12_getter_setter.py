# Python 中的 setter 和 getter 是封装类属性的核心方法，核心作用是控制属性的读写逻辑、校验数据合法性、隐藏内部实现，
# 让属性操作更安全、可控且可扩展。
class Person:
    # 函数在类中称之为方法 _init_ 是特殊方法，在创建对象时调用 主要是给当前正在创建的实例对象添加属性
    # _init_方法接受到的参数是当前正在创建的实例对象，self
    planet='moon'
    max_age=100
    def __init__(self,name,age,id_card):
        self.name=name   #公有属性 当前类 子类 实例对象可以访问
        self._age=age    #保护属性 当前类 子类可以访问，实例对象不可以访问
        self.__id_card=id_card  #私有属性 当前类可以访问，子类不可以访问，实例对象不可以访问

    # 注册age的getter方法，当实例对象访问age属性 age方法就会被自动调用
    @property
    def age(self):
        return self._age
    # 注册age的setter方法，当实例对象修改age属性 age方法就会被自动调用
    @age.setter
    def age(self,value):
        if value > self.max_age:
            print('年龄不能超过100岁')
        else:
            self._age=value

    # 私有属性也是可以使用getter与setter进行控制
    @property
    def id_card(self):
        return self.__id_card[:6]+'*****'+self.__id_card[-4:]

    @id_card.setter
    def id_card(self,value):
        print("sorry id_card can`t be modified")

P1=Person('andy',18,'123456789012345678')
print(P1.age)
P1.age=120
P1.id_card='123456789012345678'