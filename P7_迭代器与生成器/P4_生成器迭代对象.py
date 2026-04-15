# 生成器可以的实现遍历Person的实例对象
# region
class Person:
    def __init__(self,name,age,gender,address):
        self.name=name
        self.age=age
        self.gender=gender
        self.address=address

    def __iter__(self):
        yield self.name
        yield self.age
        yield self.gender
        yield self.address

p1=Person("tom",18,"male","beijing")
for item in p1:
    print(item)
#endregion
# 无论是迭代器还是生成器 都可以使用list tuple set拿到里面的内容 但是容易挤爆内存

# 生成器表达式 类似列表推导式的语法
# 语法-表达式 for 变量 in 迭代对象
nums=[1,2,3,4,5,6,7,8,9,10]
print('列表推导式')
result=[item*2 for item in nums]
print(result)
print('生成器推导式')
result1=(item*2 for item in nums)
print(result1)
print(list(result1))