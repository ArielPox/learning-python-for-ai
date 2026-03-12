# 通过 [表达式 for 变量 in 迭代对象] 生成新的列表
from P4_profound_function.P6_several_data_processing_function import result

list1=[1,2,3,4,5,6,7,8,9,10]
list2=[i*i for i in list1]
print(list2)
# 带条件的列表生成
list3=[i*i for i in list1 if i%2==0]
print(list3)

# 字典推导式
names=['andy','bob','candy']
scores=[90,80,70]
dic={names[i]:scores[i] for i in range(len(names))}
print(dic)

# 集合推导式
names1=['andy','bob','candy']
set1={i+'?' for i in names1}
print(set1)

# python中没有元组推导式 下述为生成器
result4=(n+'!' for n in names1)
print(tuple(result4))