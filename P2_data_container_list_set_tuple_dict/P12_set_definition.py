# 集合 无顺序 不能通过下标访问元素，自动去重
# 可变集合
s1={1,2,3,4,5,6,7,8,9,10,11,12,13,14,15}
s2={'hi','hello',1,2,3,4,5,6,7,8,9,10,11,12,13,14,15}
s3={1,True,'hi'}
print("无序")
print(type(s1),s1)
print(type(s2),s2)
print(type(s3),s3)
s2.add('world')
print(s2)

print(
    "不可变集合，不可以更改里面的 所有更改元素的方法也使用不了"
)
s11=frozenset(s1)
s22=frozenset(s2)
s33=frozenset({1,2,3})
print(type(s11),s11)
print(type(s22),s22)
print(type(s33),s33)

# 2.定义空集合
s4=set()
# 这样的定义的是空字典
s5={}
print(type(s4),s4)
print(type(s5),s5)

# 集合中只能存不可变的元素 可变元素不能放 由于集合不不支持下标 但是底层仍然给每一个元素分配一个编号，标号是根据内容计算得到的哈希值，
# 内容一旦变化 哈希值就会变化，就无法通过原来的哈希值找到元素