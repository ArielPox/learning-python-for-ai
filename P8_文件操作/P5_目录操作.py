import os
import shutil

# 1.os.mkdir(path)：创建单级目录 存在的话就会抛出错误
# os.mkdir('D:\Amyproject\pylearn/test')

# 2.创建多级目录 路径中所有的目录都存在就会报错
# os.makedirs('D:\Amyproject\pylearn/test/test1/test2')

# 3.删除空目录 如果目录不存在或者是非空就会报错
# os.rmdir('D:\Amyproject\pylearn/test')

# 4.递归删除空目录直到父目录不是空目录
# os.removedirs('D:\Amyproject\pylearn/test/test1/test2')

# 5.判断路径是否存在 存在返回True 目录或是文件都算
# print(os.path.exists('D:\Amyproject\pylearn/test'))

# 6.判断路径是不是存在 不存在或者是路径指向的是文件都会都会返回false
# print(os.path.isdir('D:\Amyproject\pylearn/test'))

# 7.判断是不是文件
# print(os.path.isfile('D:\Amyproject\pylearn/test/test1'))

# 8.扫描指定的目录 只有单层的
result=os.scandir('D:\Amyproject\pylearn')
# for i in result:
#     print('目录名：' if i.is_dir() else '文件名：',i.name)

# 按照层级 递归的遍历指定目录下所有的子目录与文件
# results1=os.walk('D:\Amyproject\pylearn')
# print(results1)
# for i in results1:
#     print(i)

# tip 删除有内容的目录
shutil.rmtree('D:\Amyproject\pylearn/test')
