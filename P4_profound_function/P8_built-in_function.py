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
for i in range(1,101):
    print(f'\rloading{i}%',end='',flush=True)
    time.sleep(0.1)
