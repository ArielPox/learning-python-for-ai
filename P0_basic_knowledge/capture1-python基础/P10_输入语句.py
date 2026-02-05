# 使用input获取用户的输入
age=input("age")
name=input("name")

print("用户通过input输入的全部都是字符串不可以进行算术运算，要运算就要进行数据类型转换")
age=int(age)
print(f"今年年龄是{age}名字{name}")
print(f"明年年龄{age+1}")