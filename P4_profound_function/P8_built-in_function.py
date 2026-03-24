f=open('a.txt','w',encoding='utf-8')
print(10,20,30,sep='-',end='!',file=f)

import time
# 第一种进度条
print('loading',end='')
for i in range(10):
    print('.',end='',flush=True)
print('finish',end='')

# 第二种进度条
print('loading',end='')
for i in range(1,10):
    print(f'\rloading{i}%',end='',flush=True)
    time.sleep(0.1)

print(f'abs取得绝对值：{abs(-10)}')
print(f'round小数点四舍五入 使用银行家舍入法 遇见0.5时，会向最近的偶数取整{round(10.5)}')
print(f'pow 表示次方 pow(2,3) = 2**3：{pow(2,3)}')


# enumerable 给序列添加索引
for index,value in enumerate(['a','b','c']):
    print(index,value)

# zip 可以迭代多个序列，返回一个迭代器，迭代器返回的是元组
for i,j,k in zip([1,2,3],[4,5,6],[7,8,9]):
    print(i,j,k)

# ord 可以得到字符的ASCII码
print(ord('a'))
# chr可以将ASCII码转换成字符
print(chr(97))