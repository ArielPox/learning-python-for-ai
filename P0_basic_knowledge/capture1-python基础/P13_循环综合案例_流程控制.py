print("welcome to the game you have three times to answer the question")
ans=False
# 最多玩3次 如果输入空就是没有回答 不计数
for i in range(1,4):
    print(f"welcome to the {i}th time")
    is_paly=input("继续游戏？True of False")
    if is_paly=="True":
        if i==1:
            ans=input("1+1等于几？")
            ans=(bool(int(ans)==1+1))
        elif i==2:
            ans=input("1+2等于几？")
            ans=(bool(int(ans)==3))
        elif i==3:
            ans=input("1+3等于几")
            ans=(bool(int(ans)==4))
    elif is_paly=="False":
        break;
    if ans:
        print(f"恭喜正确 你还有{3-i}次机会")
    else:
        print(f"回答错误 你还有{3-i}次机会")
print("游戏结束")



