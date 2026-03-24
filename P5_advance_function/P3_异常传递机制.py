# 异常传递机制：异常没有被当前的代码块处理 异常就会一层层的传递给其他的调用者 如果调用者都没有捕捉这个异常 程序就会因为未处理异常而意外终止
def test1():
    print('this is test 1')
    result=1+'1'
    print('test1 end')

def test2():
    print('this is test 2')
    try:
        test1()
    except Exception as e:
        print(e)
    print('test2 end')

def test3():
    print('this is test 3')
    test2()
    print('test3 end')

test3()
