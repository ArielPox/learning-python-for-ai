# 形成条件:存在嵌套函数 内部函数使用到了外部函数的变量 外层函数返回了内部函数本身
def outer_func():
    a=0
    def inner_func():
        nonlocal a # nonlocal声明使用的是外部函数变变量
        a+=1
        return a
    return inner_func

my_closure=outer_func()
print(my_closure())
print(my_closure())
print(my_closure())


# outer_fun 执行之后应该被释放 但是内部的inner_func引用了参数 变量会保存在闭包里面
# my_closure的本质是闭包对象,可以通过_closure_查看保留的变量
print(my_closure.__closure__)
print(my_closure.__closure__[0].cell_contents)
print("闭包保留的是变量的引用 并不是值 如果外层变量的是可变对象 修改会直接生效"
      "内存泄漏风险：闭包会长期保留对外部变量的引用，若闭包对象被长期持有（如全局变量），"
      "可能导致内存无法释放，需及时销毁闭包引用（f = None）。"
      "避免循环引用：闭包内部若引用了外层函数的对象，且该对象又引用闭包，可能导致垃圾回收（GC）无法清理")

print('1. 实现「私有变量」（Python 无原生私有变量，闭包是替代方案）'
      '3. 装饰器（Python 装饰器的底层就是闭包）')