# python中函数是使用def关键值定义 需要先定义再使用
def sayHi():
    print("hello")

sayHi()

# 带参数
def order_dist(num,dish):
    print(f"you had ordered {num } bowl {dish}")
order_dist(3,"大盘鸡")

# 函数传参位置参数调用函数直接传入参数值 就必须按照传参的顺序写，或者是直接时候关键字参数，指明传入的参数是属于谁的
# 关键字参数单独使用就必须是每一个数都是要用关键子参数
order_dist(dish="apple",num=2)

# 两个方法都支持：/之前就只能使用位置参数，*之后只能使用关键字参数
def rig(name,age,/,gender,*,heigh):
    print(f"{name} {age} {gender} {heigh}")
rig('andy',12,'women',heigh=188)

# 函数默认值 没有传入就使用默认值 传入就使用传入的值
def fun(msg='我是默认值'):
    print(f"{msg}")
fun()
fun('我是传入值')