# 全局作用域：变量在的当前的文件都可以任意私用
#局部作用域：只有函数的内部的作用域，函数的调用时候创建变量 函数的执行完毕就销毁局部变量与局部作用域
n=100
def test():
    global n
    n+=1;
    print(n)
test()
test()
test()

# 函数的嵌套调用与递归调用使用的是压栈处理
def test1(n):
    if n>0:
        test1(n-1)
        print(n)
test1(5)

# 函数的额活命文档，在调用的时候 会对的参数以及结果进行一个说明
def test(a,b):
    '''
    :param a: 被加数
    :param b:
    :return:
    '''
    a+=1
    return a*b
print(test(100,200))
