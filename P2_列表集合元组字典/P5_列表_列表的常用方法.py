# 所有的列表的方法都只会作用于当前层，不会作用于嵌套层

# 1.查找指定元素第一次出现的下面 index(值)
list1=[1,2,3,4,5,6,7]
print(list1.index(6))

# 2.统计某元素在list中出现的次数 count(值)返回次数
list2=[1,2,1,2,1,4,3,4,7,[1,2,2,1,1,1,1,1]]
print(list2.count(1))

# 3.反转列表reverse()
list3=[1,2,3,4,5,6,7,[1,2,2,1,1,1,1,1]]
list3.reverse()
print(list3)

# 4.对元素排序 默认从小到大 sort(reverse='True/False'),reverse参数会改变排序方式

list4=[1,2,3,4,5,54,21,13,65,77,6,7]
list4.sort()
print(list4)
list5=[1,2,3,4,5,54,21,13,65,77,6,7]
list5.sort(reverse=True)
print(list5)
# 列表中有数字和字符串 排序会失败报错 如都是字符串会具字符的Unicode编码排序
list6=['lily','top','hhelo','word']
list6.sort()
print(list6)


