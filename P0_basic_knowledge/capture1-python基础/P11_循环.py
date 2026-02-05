# 使用for循环遍历range所指的数字的范围
from tokenize import group

print("range()的取数的范围是左闭右开")
for n in range(1,11):
    print(f"this is {n}")

for i in 'abcd':
    print(f"this is {i}")

h=1
while h<=10:
    print("while打印只要条件满足就会一直运行",h)
    h+=1

print("嵌套循环")
day=1
while day<=10:
    print(f"******this is {day} day********")
    sport=1
    while sport<=3:
        print(f"this is {sport} sport")
        sport+=1
    day+=1

print("the exercise is over")
