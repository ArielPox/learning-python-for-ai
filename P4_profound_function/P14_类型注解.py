# 1.变量类型注解
num:int=100
price:float=99.9
name:str='andy'
is_true:bool=True

# 可以先类型注解再赋值
school:str
school='pku'
print(type(school))

# 列表注解
list1:list[int]=[1,2,3,4]

list2:list[str]=['andy','tom']

# hobby是列表
hobby:list[str | int]=['football',1]
# 旧版的写法
from typing import Union
hobby1:list[Union[str,int]]=['football',1]


# city是集合
city:set[ str]={'beijing','shanghai'}
# 可以是多种类型
city1:set[str | int]={'beijing',1}

# 字典str是键 int是值
dict1:dict[str,int]={'name':'andy','age':18}

# 元组比较特别一点的是 tuple[int]只能是一个int元素
tuple1:tuple[int]=(18)

# 表示多个一样的 元素
tuple2:tuple[int,...]= (18,18,18)

# 表示多个类型的 元素
tuple3:tuple[str | int,...]= (18,'andy')

# python会根据初始赋值的变量类型：对于普通的变量 后续改变的类型的 不会告警
# 对于容器变量：对于容器变量 改变的元素类型 会告警

# 函数的类型注解
# 语法格式def func(参数:参数类型)->返回值类型:
def add1(x:int,y:int)->int:
    return x+y

def add2(x=1,y=2)->int:
    return x+y

# 设置多个返回指的类型注解
def show_nums_info(nums:list[int])->tuple[int,int,float]:
    return (len(nums),max(nums),min(nums))
print(show_nums_info([1,2,3,4,5,6,7,8,9]))


# 使用*args类型注解要求每一个数都是的int类型
def add_nums(*args:int)->int:
    rs
print(add_nums(1,2,3,4,5,6,7,8,9))

# 使用**kwargs的类型注解 要求数据为int或float
def show_info(**kwargs:int | float)->dict[str,int | float]:
    return kwargs
print(show_info(name='andy',age=18))

# 获取函数的注解信息
# 函数.__annotations__
print(show_nums_info.__annotations__)