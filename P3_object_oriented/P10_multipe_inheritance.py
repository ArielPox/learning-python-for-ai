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
        print(f"show the parent msg:{msg}")

class Worker:
    def __init__(self,workplace,salary):
        self.workplace=workplace
        self.salary=salary

class Student(Person,Worker):
    def __init__(self,name,age,score, grade,workplace,salary):
        # 多重继承可以显示调用父类的方法
        Person.__init__(self,name,age)
        Worker.__init__(self,workplace,salary)
        self.score=score
        self.grade=grade

S=Student('andy',18,100,'A','beijing',1000)
print(S.__dict__)
print("_mro_可以查看的属性与方法的查找方法")
print(Student.__mro__)