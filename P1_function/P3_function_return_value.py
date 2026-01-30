# 函数执行之后 会把结果交给调用者 这个结果就是函数的返回值 return 会将函数的执行的结果返回给调用者的 没有return的话就会默认返回的None
def test(a,b):
    print(a,b)
result=test(100,200)
print(result)
#return 后面的值会返给调用者
def test1(a,b):
    return a+b
result1=test1(100,200)
print(result1)
#