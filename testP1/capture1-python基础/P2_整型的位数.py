import sys
print("当数据很大的时候 可使用下划线将数据的分组，增强可读性")
salary=3000_000

print(salary)

#python的整数的上限数值，取决于执行代码的计算机的内存与处理能力
a=9**9999
#可以控制python的不限制的展示数值的长度 否则超出计算机长度的就会报错 ：
# ValueError: Exceeds the limit (4300 digits) for integer string conversion; use sys.set_int_max_str_digits() to increase the limit
# python打印字符换的时候转化为了字符串打印
sys.set_int_max_str_digits(0)
print(a)