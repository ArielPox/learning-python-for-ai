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

    def run(self,distance):
        print(f"{self.name} run {distance} meters")

    # 使用@classmethod装饰的方法 称之为类方法，类方法不需要实例对象，类方法第一个参数是类对象cls
    # 类方法接收到的是本身cls 是可以访问到得类的属性 可以实现的与类相关的一些信息与工厂函数，实例对象也可以调用 但是不推荐
    @classmethod
    def test1(cls,data):
        cls.planet=data
        print(f"this is a classmethod {cls.planet}")

    @classmethod
    def create(cls,strinfo):
        name,age=strinfo.split('-')
        return cls(name,age)

Person.test1('earth')
print(Person.__dict__)

P2=Person.create('andy-18')
print(P2.__dict__)