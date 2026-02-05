# 集合A中不同于集合B的元素 返回一个集合
A={12,13,14}
B={13,14,15}
result1=A.difference(B)
print(result1)

# 集合A中删除的集合B存在的元素
A.difference_update(B)
print(A)

# 合并A与B返回一个新集合
resultAB=A.union(B)
print(resultAB)

# 判断A是不是集合A的子集
print(A.issubset(B))

print("判断A是不是包含了B的所有元素")
print(A.issuperset(B))
print(resultAB.issuperset(B))

print("判断AB是不是有交集")
print(A.isdisjoint(B))

