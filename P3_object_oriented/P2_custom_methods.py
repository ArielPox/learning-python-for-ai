# 定义类使用大驼峰写法
class Person:
    # 函数在类中称之为方法 _init_ 是特殊方法，在创建对象时调用 主要是给当前正在创建的实例对象添加属性
    # _init_方法接受到的参数是当前正在创建的实例对象，self
    def __init__(self,name,age):
        self.name=name
        self.age=age

    # 在类里面定义的函数作为方法可以被所有的示例对象调用
    def show(self,msg):
        print(f"show the {msg}")

P1=Person('andy',18)
# 示例对象查找方法，先从自身查找方法，没有再从类中查找
P1.show('hehe')

def show():
    print("show the instantiated Object")
P1.show=show
P1.show()

print(P1.__dict__)
print(Person.__dict__)

