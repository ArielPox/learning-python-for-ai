# 元组不可增删改，可以查
# 1.定义元组
t1=(1,2,3,3)
t2=('andy','ttom')
t3=(100,True,'hi',None)
t4=(100,[1,2,3,4],'hi',(5,6,7,8))
print(type(t1),t1)
print(type(t2),t2)
print(type(t3),t3)
print(type(t4),t4)

# 2.定义空tuple
t5=()
t6=tuple()
print(type(t5),t5)
print(type(t6),t6)

# 3.元组的下标
t7=(5,6,7,8,9,9)
print(type(t7),t7[2])
print(type(t7),t7[-1])

# 4.元组中的元组是不可以更改的，但是的元组中的元素是可更改的数据类型比如列表就是的可以深层改变的
t8=(1,2,3,[22,33,44,55])
t8[3][1]=100
print(type(t8),t8)
# 会报错：TypeError: 'tuple' object does not support item assignment
# t8[2]=1000
# print(type(t8),t8)

# 5.元组的常用方法 t.index()会返回元素出现的首个位置的index
t9=(6,7,8,9,9)
res=t9.index(9)
print(res)

# count(num) 会统计指定元素出现的次数
res2=t9.count(9)
print(res2)

# 6.元组的常用的内置函数
p1=(1,2,3,4,5)
print(max(p1))
print(min(p1))
print(sum(p1))
print(len(p1))

# sorted函数对元组的排序，不会修改的元组 会返回的一个新的list 需可以使用tuple转换
p2=[2,4,7,13,545,77,989,11]
res3=sorted(p2,reverse=True)  #数据大到小
print(res3)
p3=tuple(res3)