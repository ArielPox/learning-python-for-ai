# 增
# add()在集合里面的添加元素
s1={1,2,3,4}
s1.add(5)
print(s1)

# update() 向集合里面添加元素的 批量
s2={2,3,4,6}
s2.update([80,90])
s2.update((100,10))
s2.update({888,'ni'})
s2.update(range(333,339))
print(s2)


# 2.删
# remove()删除指定元素 元素不存在就报错
s3={3,4,5}
s3.remove(5)
print(s3)

# discard()删除指定元素，元素不存在不报错
s4={9,8,7,3}
s4.discard(6)
print(s4)

#
print("pop任何删除一个元素 返回")
s5={831,2,3,1,2,3,5,845,23,4,67,78,121}
result=s5.pop()
print(s5)
print(result)

print("清空集合")
s5.clear()
print(s5)


print("集合没有下标，也不支持分片，故不支持按位置访问的能力，可以使用in运算符判断是不是存在指定的元素")
s6={1,2,3,4,5}
print(2 in s6)
print(3 not in s6)