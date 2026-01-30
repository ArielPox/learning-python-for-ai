class Person:
    # 函数在类中称之为方法 _init_ 是特殊方法，在创建对象时调用 主要是给当前正在创建的实例对象添加属性
    # _init_方法接受到的参数是当前正在创建的实例对象，self
    planet='moon'
    max_age=100
    def __init__(self,name,age,gender):
        self.name=name   #公有属性 当前类 子类 实例对象可以访问
        self._age=age    #保护属性 当前类 子类可以访问，实例对象不可以访问
        self.__gender=gender  #私有属性 当前类可以访问，子类不可以访问，实例对象不可以访问

    # 在类里面定义的函数作为方法可以被所有的实例对象调用 这些方法称之为实例方法
    def show(self,msg):
        print(f"show the parent msg:{msg}")

class Student(Person):
    def __init__(self,name,age,score, grade):
        super().__init__(name,age)
        self.score=score
        self.grade=grade

P1=Person('andy',18,'male')
print(Person.__dict__)
print(P1.__dict__)
print("保护属性也可以访问 但是不推荐")
print(P1._age)
print("私有属性不可以访问 会报错")
# print(P1.__gender)

# python底层通过重命名的方式实现私有属性
print(P1._Person__gender)