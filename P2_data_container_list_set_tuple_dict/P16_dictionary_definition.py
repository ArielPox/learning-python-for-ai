d1={'andy':99,'tom':88}
print(type(d1),d1)

print("字典中的key不可以重复，重复的话后面的会覆盖之前")

print("空字典")
d2={}
d3=dict()
print(type(d2),d2)
print(type(d3),d3)

print("字典中的key必须是不可变类型，value可以是任意类型")
d4={22:10,'andy':10}
print(type(d4),d4)

print("字典可以嵌套")
d5={'andy':{'age':10,'gender':'women'},'tom':19}
print(type(d5),d5)