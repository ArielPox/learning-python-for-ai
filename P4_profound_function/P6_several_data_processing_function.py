# 语法格式：map(操作函数，迭代对象)
nums=[10,20,30]
def doublen( n):
    return n*2
result=list(map(doublen,nums))
#map返回的是一个迭代器对象，需要手动遍历
print(list(result))

# eg2:字符串转换
names=('andy','bob','candy')
result1=list(map(str.upper,names))
print(tuple(result1))

# eg3 类型转换
str_num={'1','2'}
result2=list(map(int,str_num))
print(set(result2))

# filter过滤器
nums2=[10,20,30,40,-1]
result3=list(filter(lambda n:n>0,nums2))

people=[
    {'name':'andy','age':35}
    ,{'name':'bob','age':25}
    ,{'name':'candy','age':45}
    ,{'name':'danny','age':15}
    ,{'name':'eddy','age':35}
]
result4=list(filter(lambda p:p['age']>30,people))
print(result4)

# filter不会立即筛选只有在需要结果的时候在执行，返回迭代的迭代器对象
#一旦遍历完成就被耗尽 可能影响元素的个数

# filter的特殊用法 如果没有传递过滤函数 就会自动的过滤掉假值
data1=[0,1,'',[],{},(),1,2,3,None,10]
result3=filter(None,data1)
print(list(result3))


# sorted函数：对一组数据排序 返回新的数据 sorted(可迭代对象,key=**,reverse=False)
nums=[10,20,30,40,50,60]
result5=sorted(nums,reverse=True)
print(result5)

# 按照字符串长度排序
names=['python','java','c']
result6=sorted(names,key=len,reverse=False)
print(result6)

# 按照字典中的某一个字段排序
persons=[
    {'name':'andy','age':35},
    {'name':'bob','age':25},
    {'name':'candy','age':45},
    {'name':'danny','age':15},
    {'name':'eddy','age':35}
    ,{'name':'fanny','age':35}
]

result7=sorted(persons,key=lambda p:p['age'],reverse=False)
print(result7)


# max函数与min函数也可以传递key
print(max(persons,key=lambda p:p['age']))
print(min(persons,key=lambda p:p['age']))


# reduce函数：对一组数据进行聚合操作 reduce(操作函数,可迭代对象)
from functools import reduce

# 数值统计
nums=[10,20,30,40,50,60]
# 其中10表示初始值
result8=reduce(lambda a,b:a+b,nums,10)
print(result8)

#字符串拼接
str_list=['as,','ndd']
result9=reduce(lambda a,b:a+b,str_list)
print(result9)