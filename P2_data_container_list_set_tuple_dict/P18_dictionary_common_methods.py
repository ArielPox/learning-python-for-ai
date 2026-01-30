d1={'andy':18,'tomm':19}

print("keys方法的返回值是dict_keys类型 可以被遍历 但是不可以通过下标访问元素")
result1=d1.keys()
for key in result1:
    print(key)
print("value同样 获得的是所有的值")
res2=d1.values()
for value in res2:
    print(value)

print("item直接获得全部键值对 返回的是元组")
res3=d1.items()
for item in res3:
    print(item)
print(res3)

print("字典没有下标 只可以通过for便利 不可以使用while")
for key in d1:
    print(f"key: {key}, value: {d1[key]}")

for key in d1.keys():
    print(f"key: {key}, value: {d1[key]}")
