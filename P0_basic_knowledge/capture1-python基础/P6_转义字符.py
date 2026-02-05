# 1使用\输出“
print("输出\"")

# 2.使用\n换行
print("换行\n输出")

# 3.使用\\输出\
print("输出\\")

# 4.使用\b删除掉前一个字符
print("hellooo\b")

# 5.使用\r回到本行开头 将后面的内容覆盖输出
print("100%\r88%")

# 6.使用\t让光标后的值基于当前的制表位跳到下一个制表位 不同的环境的制表位数是不一样的 pycharm里面是4位
print('123412341234')
print('ab\tcd')
print('abc\td')
print('abcd\ta')
print("可以使用expandtabs强制的更改制表位")
print('123412341234')
print('ab\tcd'.expandtabs(8))
print('abc\td'.expandtabs(8))
print('abcd\ta'.expandtabs(8))