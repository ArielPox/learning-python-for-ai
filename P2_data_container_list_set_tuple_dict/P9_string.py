# 字符串就是存放一个个字符的数据容器
msg='hhhhaaaakkkk'
print(msg[3])

# 字符串的字符是不可以更改的字符串不可以嵌套会报错 TypeError: 'str' object does not support item assignment
# msg[4]='m'
# print(msg)

# 2.字符串的 常用方法
# index(str)返回目标字符出现的第一个位置
msg1='hi,lo,ha,la,xi,zk,ccl'
print(msg1.index('x'))

# split可以将字符串按照指定的字符进行分割 返回一个列表
print(msg1.split(','))

#replace（‘被替换’，‘目标’） 将字符串的某一个片段更改为目标的片段
msg2='hello,word'
print(msg2.replace('w','WWW'))

# strip()从字符串的两端删除，知道遇到第一个不在目标字符串的第一个字符
msg3='34341234421this1234,4321and3421'
print(msg3.strip('1234'))
# 不传入参数的就会去除字符串两端的空格
msg4='    hi    '
print(msg4)
print(msg4.strip())