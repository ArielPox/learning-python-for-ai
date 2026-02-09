# 函数返回的多个值 会采用元组的方式返回
def fun1(a,b):
    return a+b,a*b

result1=fun1(10,20)
print(result1)

# 2.打包接收的参数
# *args代表打包的是位置参数形成的是一个元组 **kwargs代表打包的是关键字参数 会形成一个字典
def fun2(*args,**kwargs):
    print(args,kwargs)

fun2(10,20,30,name='andy',age=35)


# 3.解包传递的参数 *变量名将元组拆为一个个独立的位置参数，**变量名可以将字典拆解为key=value的形式的关键字参数
def fun3(num1,num2,num3,name,age,gender):
    print(num1,num2,num3)
    print(name,age,gender)

t1=(10,20,30)
d1={'name':'andy','age':35,'gender':'male'}
fun3(*t1,**d1)

