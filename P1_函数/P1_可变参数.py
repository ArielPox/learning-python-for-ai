# 位置参数传入元组 *接受的就是的一个的元组
def test(*args):
    print(args)
test(1,2,3,4,'andy','tom')

#位置的参数传入字字典
def test1(**kwargs):
    print(kwargs)
# 调用函数
test1(name='andy',age='18')

# 传入参数顺序：位置参数，元组，字典
def test2(a,b,*args, **kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)

# 调用函数的
test2('this is a','this is b','andy',12,'women',address='beijing',say='hello')