# 字符串在简单的“+”拼接只对字符串有效 不可以有其他数据类型的变量拼接会比较麻烦
name="张三"
gender="male"
age=111
weight=45.8
print("使用占位符拼接比较麻烦")
print("方法二使用占位符")
print("%s-占位字符串，%f占位浮点数，%i占位整数，%d占位十进制整数，其中%s是万能的 会将所有数据类型转换为字符串之后打印")
info1="姓名为%s,性别%s,体重%f,年龄%d" % (name,gender,age,weight)
print(info1)

print("方法3-使用f-string 将占位的内容的使用字符串方式插入进来--推荐")
info3=f"姓名{name},性别{gender}，体重{weight}，年龄{age}"
print(info3)