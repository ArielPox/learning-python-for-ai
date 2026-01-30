d1={}
# 新增
d1['andy']=25
d1['tom']=22
d1['lily']=33
print(d1)
print("查询 直接查询不存在会报错")
# print(d1['lisa'])
print(d1['lily'])
print("使用get 不存在返回none")
print(d1.get('andy'))
print(d1.get('tomm'))

print("修改：直接修改")
d1['tom']=1000
print(d1)

print('批量修改或者是合并多个键值对')
d1.update({'tom':999,'lili':12})
print(d1)

print("删除 del 删除指定的 不存在就报错，pop弹出对应额，可以设默认值，不存在的时候展示默认值，clear全部清空")
del d1['tom']
print(d1)
print(d1.pop('w',"目标值不存在"))
d1.clear()
print(d1)
