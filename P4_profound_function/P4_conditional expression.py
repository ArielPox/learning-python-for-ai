# 表达式执行之后可以得到的一个值的就是表达式
# 条件表达式：根据条件真假 在两个结果中二选一 又称之为三元表达式三目运算符
print("条件表达式: 值 if 条件1为true else 值2")
age=19
text='adult' if age>=18 else age<18
print(text)

is_vip=True
discount=0.8 if is_vip else 1
print(discount)
