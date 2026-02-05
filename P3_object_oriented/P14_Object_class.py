# python中所有的类都继承了Object类，所有的对象好包含str int bool list tuple set都是Object的子类
class Person:
    planet='moon'
    max_age=100
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender

P1=Person('amdy',19,'women')

print(isinstance(P1,Person))
print(isinstance(P1,object))
print(isinstance(1,object))
print(isinstance('andy',object))
print(isinstance('True',object))
print(isinstance(None,object))
print(isinstance(True,object))

print("查看object的方法")
# for key in object.__dict__:
#     print(key)
print('check the attribution and methods which come from parent and self')
print(dir(P1))
print(P1.__str__())
print(P1)

