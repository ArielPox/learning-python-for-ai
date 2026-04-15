import os

# 日志记录
# 1.用户输入用户名与密码之后 程序校验
# 2.用户名不存在 提示未注册并且记录到日志
# 3.存在但是密码错误 提示密码错误并且记录到日志
# 4.用户与密码正确 提示成功并且记录到日志

uses={
    'andy':'123456',
    'tom':'279269',
    'jerry':'123456'
}

username=input('请输入用户名：')
password=input('请输入密码：')
if username in uses and uses[username]==password:
    print('登录成功')
    with open('logs/log.txt','a',encoding='utf-8') as f:
        f.write(f'{username}登录成功\n')
elif username not in uses:
    print('用户不存在')
    with open('logs/log.txt','a',encoding='utf-8') as f:
        f.write(f'{username}用户不存在\n')
else:
    print('密码错误')
    with open('logs/log.txt','a',encoding='utf-8') as f:
        f.write(f'{username}密码错误\n')