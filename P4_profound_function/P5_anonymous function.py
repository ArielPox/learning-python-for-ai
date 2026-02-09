# 匿名函数：python 中的匿名函数使用lambda 来定义 格式为：lambda 参数：表达式
# 特点：1.只能写一行代码 不能写多行代码。2.不能写代码块。
# 3.冒号的右边必须是表达式 只能写一个表达式。4.b表达式结果自动作为返回值
def caculate(func,b,c):
    return print(f'{func(b,c)}')

# 匿名函数作用就是做很小的事儿
caculate(lambda a,b:a*b,10,20)
caculate(lambda a,b:a//b,10,20)
