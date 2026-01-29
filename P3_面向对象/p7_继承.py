class Person:
    # 函数在类中称之为方法 _init_ 是特殊方法，在创建对象时调用 主要是给当前正在创建的实例对象添加属性
    # _init_方法接受到的参数是当前正在创建的实例对象，self
    planet='moon'
    max_age=100
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def speak(self,msg):
        print(f"{self.name} say {msg}")

# 定义一个Student继承父类 超类 基类
class Student(Person):
     #在子类两个方式调用父类的初始化方法实现继承
      def __init__(self,name,age,score):
          # 方法1：使用super
          # super().__init__(name,age)
          # 方法2：使用父类名
          Person.__init__(self,name,age)
          # 子类特有的部分需要手动完成初始化
          self.score=score


S1=Student('andy',18,100)
print(S1.__dict__)
# 子类使用方法 使用冒泡的方式往上找方法
S1.speak('hi')

