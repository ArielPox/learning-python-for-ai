# 1.使用while
list1=[10,20,30,40,50,60,70,80,90]
print("使用while")
index=0
while index<len(list1):
    print(list1[index],end=' ')
    index+=1

# 使用for循环
print("使用for")
for item in list1:
    print(item,end=' ')


for index in range(len(list1)):
    print(list1[index],end=' ')

print("使用for遍历，通过enumerable(list,start)可以指定从多少开始,改变的是的循环的编号而不是 真的index")
for index,item in enumerate(list1,start=2):
    print(index,item)
