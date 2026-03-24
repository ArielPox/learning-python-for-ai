# 当程序遇到不符合情况的额误时，会抛出一个异常，异常会传递给调用者，调用者会处理异常。
# 1.try except

try:
    a=int(input('请输入数字：'))
    b=int(input('请输入数字：'))
    result=a / b
    if result < 0:
        raise ValueError('结果不能小于0')
    print(f'a/b={result}')
except ZeroDivisionError:
    print('除数不能为0')