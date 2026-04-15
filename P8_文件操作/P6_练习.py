# 将文件复制到另一个文件里面
import os


source='../test/test1.txt'
target='../test/target.txt'

# ... existing code ...
with open (source,'rb') as f1,open(target,'wb') as f2:
    while True:
        data=f1.read(1024)
        if not data:
            break
        f2.write(data)
    print('文件复制完成')
