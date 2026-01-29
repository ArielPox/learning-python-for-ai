class Person:
    # 函数在类中称之为方法 _init_ 是特殊方法，在创建对象时调用 主要是给当前正在创建的实例对象添加属性
    # _init_方法接受到的参数是当前正在创建的实例对象，self
    def __init__(self,name,age):
        self.name=name
        self.age=age

    # 在类里面定义的函数作为方法可以被所有的实例对象调用 这些方法称之为实例方法
    def show(self,msg):
        print(f"show the {msg}")

    def run(self,distance):
        print(f"{self.name} run {distance} meters")

print(Person.__dict__)
P1=Person('andy',18)
P2=Person('tom',19)
P1.show('hehe')
P2.run(1000)

# 通过类调用实例方法
Person.show(P1,'haha')
Person.run(P2,2000)