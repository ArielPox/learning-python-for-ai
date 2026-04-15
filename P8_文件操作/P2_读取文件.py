# 读取文件：创建文件对象 操作文件 关闭文件
# 文件操纵的核心：open(filename,mode, encoding)其中
# filename 要操作的文件的路径
# mode 模式 r:只读 w:只写 a:追加 rb:二进制读 rb+:二进制读写 wb:二进制写 wb+:二进制读写,rt:文本读,
# encoding 指定文件的编码格式

# 创建文件对象
# region

f=open(file='test.txt',mode='rt',encoding='utf-8')
# 操作文件
print(f.read())
# 关闭文件
f.close()
# endregion

# 读写操作1:使用文件对象的read方法 读物文件中的内容 热read（)方法会一次性读取文件的内容,read(size)方法会一次性读取指定大小的内容,这个size指的是字符的个数
# read()会从上一次读取的位置继续读取，达到文件末端继续读就会返回空字符
# region
f=open(file='test.txt',mode='rt',encoding='utf-8')
print(f.read(6))
f.close()
#endregion
print('# 读写操作2:使用文件对象的readline方法 读物文件中的内容的一行')
# readline()方法会从上一次读取的位置继续读取，达到文件末端继续读就会返回空字符
#readline（size)中的size标识读取当前行的时候 最多可以读取的字符数
# region
f=open(file='test.txt',mode='rt',encoding='utf-8')
print(f.readline(10))
print(f.readline())
f.close()
#endregion

print('使用for循环遍历文件对象')
# region
f=open(file='test.txt',mode='rt',encoding='utf-8')
for line in f:
    print(line)
f.close()
#endregion

print('使用readlines(hint)读取对象会返回一个列表，每一行占一个列表位')
# region
# hint是可选的参数 不传递就表示读取当前文件的所有行
# 传递就表示期望读取的字符个数的 readlines(hint)会一次性读取文件的所有的内容 不合适大文件的读取
f=open(file='test.txt',mode='rt',encoding='utf-8')
for item in f.readlines():
    print(item)
f.close()
#endregion

print('最佳实践是使用with上下文管理器，结合for循环遍历')
# region
with open(file='test.txt',mode='rt',encoding='utf-8') as f:
    for item in f:
        print(item)

