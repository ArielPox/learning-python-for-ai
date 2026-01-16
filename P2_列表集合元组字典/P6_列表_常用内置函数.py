# 1.使用内置的sorted函数 会返回一个排序之后的新容器
# 都是数据就会按照数字大小升序 若有数字有字符会报错，都是字符就会按照Unicode编码排序 其他的方法也是使用
nums=[22,24,5,3,2]
result=sorted(nums,reverse=True)
print(result)

nums1=['andy','tom','tttt']
result1=sorted(nums1,reverse=True)
print(result1)

# 2.len(nums)会返回元素个数
nums2=[1,2,3,2,3,4,[9,1,2,3,3,4,8,5,1,66,]]
print(len(nums2))

# 3.返回的容器中的最值与和
nums3=[1,2,3,3,4,5,6]
print(max(nums3))
print(min(nums3))
print(sum(nums3))