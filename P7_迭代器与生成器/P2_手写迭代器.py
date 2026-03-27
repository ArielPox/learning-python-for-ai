# target

# for可以遍历person的实例对象
# 方法1
#region
class Person:
    def __init__(self,name,age,gender,address):
        self.name=name
        self.age=age
        self.gender=gender
        self.address=address

    # 定义一个私有的迭代器
    def __iter__(self):
        return PersonIterator(self)

# 手写迭代器
class PersonIterator:
    def __init__(self,person):
        # 将外部传入的数据保存好
        self.person=person
        self.index=0
        # 配饰好需要遍历的内容
        self.attrs=['name','age','gender','address']

    # 迭代器会返回迭代器自身
    def __iter__(self):
        return self

# 定义next方法
    def __next__(self):
        if self.index>=len(self.attrs):
            raise StopIteration
        # 获取要返回的内容
        value=self.attrs[self.index]
        #更新迭代器的位置
        self.index+=1
        return value

p1=Person("tom",18,"male","beijing")
for item in p1:
    print(item)

#endregion

# 方法2
#region
class Person:
    def __init__(self,name,age,gender,address):
        self.name=name
        self.age=age
        self.gender=gender
        self.address=address

    # 定义一个私有的迭代器
    def __iter__(self):
        return PersonIterator(self)

# 手写迭代器
class PersonIterator:
    def __init__(self,person):
        # 将外部传入的数据保存好
        self.person=person
        self.index=0
        # 配饰好需要遍历的内容
        self.attrs=['name','age','gender','address']

    # 迭代器会返回迭代器自身
    def __iter__(self):
        return self

# 定义next方法
    def __next__(self):
        if self.index>=len(self.attrs):
            raise StopIteration
        # 获取要返回的内容
        attr_name=self.attrs[self.index]
        value=getattr(self.person,attr_name)
        #更新迭代器的位置
        self.index+=1
        return value

p1=Person("tom",18,"male","beijing")
for item in p1:
    print(item)

#endregion

