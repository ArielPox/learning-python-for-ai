print("boolean 只有两个值 首字母大写 Ture 与False，python中的除了0之外的所有的值转化为bool值之后都是true")
print("python中除了空字符串以外的任何字符换转化为bool()都是true")
print(bool(' '))

print("逻辑运算符有and or not")
print("and 返回的不一定都是布尔值 他返回的为某个参与计算的值的本身。and会先看左边左边为假就直接返回左边 否则直接返回右边"
      "若参与and运算的不是bool值 python会自动转为bool值 然后再进行逻辑操作")
print(2-2 and True)
print('' and True)
print(True and 8//3)
print(2 and 999)

print("or 返回的不一定都是布尔值 他返回的为某个参与计算的值的本身。or会先看左边,左边为真就直接返回左边 否则直接返回右边"
      "若参与or运算的不是bool值 python会自动转为bool值 然后再进行逻辑操作")
print(2-2 or True)
print(bool('') or False)
print(True or 8//3)
print(2 or 999)

print("not表示取反 若参与not运算的不是bool值 python会自动转为bool值 然后再进行逻辑操作,not返回的值一定是布尔值")
print(not True)
print(not 3>2)