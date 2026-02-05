from langchain_community.document_loaders.notiondb import DATABASE_URL

print('指的是同一个方法名 在不同的对象上调用的时候呈现出不同行为 必须满足 继承与方法重写')
# standard polymorphism
class Animal:
    def speak(self):
        print('animal are speaking')

class Dog(Animal):
    def speak(self):
        print('dog wangwang')

class Cat(Animal):
    def speak(self):
        print('cat miaomaio')

class Pig:
    def speak(self):
        print('pig pig')

def ani_speak(animal:Animal): #类型注解 要求传入animal必须是Animal的子类
    animal.speak()

d=Dog()
c=Cat()
# 在python里面指明类型限制但是没有继承关系 不会报错 但是不推荐使用
p=Pig()
ani=Animal()

ani_speak(ani)
ani_speak(d)
ani_speak(c)
ani_speak(p)
