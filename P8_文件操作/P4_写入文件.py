# 文件操纵的核心：open(filename,mode, encoding)其中
# filename 要操作的文件的路径
# mode 模式 r:只读 w:只写 a:追加 rb:二进制读 rb+:二进制读写 wb:二进制写 wb+:二进制读写,rt:文本读,
# encoding 指定文件的编码格式

# 测试w模式：写入 并且覆盖
f=open(file='test2.txt',mode='wt',encoding='utf-8')
f.write('hello world')
f.close()

#测试x模式：作用是创建文件，如果文件已经存在会抛出异常
# f=open(file='test3.txt',mode='xt',encoding='utf-8')
# f.write('hello world')
# f.close()

# 测试a模式：追加
# f=open(file='test3.txt',mode='at',encoding='utf-8')
# f.write('hello world')
# f.close()

#文件对象的flush方法：python中写入文件 不是一次就写进去的，而是会先写入缓冲区，
# 当缓冲区满了之后才会写入文件，但是python没有提供缓冲区满之后立即写入文件的方法，但是可以通过flush方法实现
f=open(file='test3.txt',mode='at',encoding='utf-8')
f.write('hello world_FLUSH')
f.flush()
f.close()
print('文件对象close方法：关闭文件对象')

#rt+模式：这个模式作用是读写文件，其中seek(offset,whence)方法可以设置文件读取的位置，
# offset:表示偏移量，表示从参考点开始读取的字节数
# whence:代表参考点，默认是0，表示从文件开头开始读取，1表示从当前位置开始读取，2表示从文件末尾开始读取
# 文本模式下 避免的定位中文字符位置，会乱码
with open(file='test3.txt',mode='rt+',encoding='utf-8') as f:
    f.write('hello world')
    f.seek(0)
    print(f.read())

# 其他的模式
#wt+：同w模式，但是会清空文件
#at+：同a模式，但是会清空文件
# xt+：同x模式，但是会清空文件