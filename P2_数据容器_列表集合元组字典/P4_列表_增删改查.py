# 增加
# method1:append在列表的尾部追加

list1=[1,2,3]
list1.append(4)
print(list1)

# method2：inser（index,num)在指定位置插入
list2=[1,2,3]
list2.insert(1,'andy')
print(list2)

# method3:方法如下
list3=[1,2,3]
list3.extend([4,5,6])
print(list3)
list3.extend('andy')
print(list3)
list3.extend(range(20,25))
print(list3)

print("删除匀元素右4个方法")
# method1：pop（index)会删除指定位置的元素 并且返回
print(list3.pop(1))
print(list3)

# method2:remove(num)会删除列表第一次出现的num
list3.remove(4)
print(list3)

# method3:删除指定元素del num[index]
del list3[0]
print(list3)

# method4:clear()将列表清空
list3.clear()
print(list3)

print("修改")
list4=[1,2,3,4,5,6,7]
list4[5]='modify'
print(list4)

print("查询直接使用下标")