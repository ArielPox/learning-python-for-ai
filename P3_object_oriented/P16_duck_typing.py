# 鸭子多态 看什么就是什么 调用什么就是什么 不需要继承 无关方法重写
# standard polymorphism
class Animal:
    def speak(self):
        print('animal are speaking')

class Dog:
    def speak(self):
        print('dog wangwang')

class Cat:
    def speak(self):
        print('cat miaomaio')

class Pig:
    def speak(self):
        print('pig pig')

def ani_speak(animal):
    animal.speak()

d=Dog()
c=Cat()
p=Pig()
ani=Animal()

ani_speak(ani)
ani_speak(d)
ani_speak(c)
ani_speak(p)