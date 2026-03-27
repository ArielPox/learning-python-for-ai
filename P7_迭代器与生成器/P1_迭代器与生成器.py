# 1、可以被for遍历的对象就是可迭代对象 iterable ,可迭代对象可以调用_iter_方法得到迭代器iterator iter(iterable)== iterable.__iter__()
# __iter__是一个魔法方法 调用iter就会调用__iter__方法
# 2、迭代器对象可以调用_next_方法得到下一个元素 同样的是一个魔法方法 调用next()方法会调用__next__方法
# region
name=["tom","jerry","lucy"]
iterator=iter(name)  #取得迭代器对象
print(next(iterator))
print(next(iterator))
print(next(iterator))
# print(next(iterator))# tip:当所有的元素都去取出之后再调用next 会抛出StopIteration异常
#endregion

# for 背后的逻辑
#region
name=["tom","jerry","lucy"]
it=iter( name)
while True:
    try:
        print(next(it))
    except StopIteration:
        break
#endregion

# 迭代器(iterator )也有__iter__方法 并且值是迭代器的自身
# 设计的原因是由于为了让for也可以遍历迭代器
#region
# Python 的 for 循环、list ()、tuple () 等所有迭代语法，只认「可迭代对象」。
# 它们的工作流程是固定的：
# 拿到一个对象
# 自动调用 iter(对象) → 获取迭代器
# 不断调用 next(迭代器) 取值
# 关键矛盾：
# 迭代器本身是用来取值的，但如果它的 __iter__ 不返回自己，它就不是可迭代对象，就不能被 for 循环使用
#endregion

# 迭代器是一次性的 状态只会向前推进，不会重置在迭代过程中会被消耗
# 迭代器对象只能被next()调用一次，不能重复调用，否则会抛出StopIteration异常

# 迭代器是惰性计算 不会一次性生成所有的结果,可以显著的降低内存的占用
# 数据量非常大的时候 不确定要多少的结果的时候 可以使用迭代器
