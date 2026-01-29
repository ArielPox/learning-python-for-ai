fruits={'appe':10,'strawberry':20,'cherry':30}

# 打印全部的水果
for key in fruits:
    print(fruits[key])

print("打印最贵的水果，根据value值返回key值")
key1=max(fruits,key=fruits.get)
print(f"the most expensive is{key1},price is {fruits[key]}")

#统计学生的成绩
stu_scores=[
    {'name':'andy','score':{'math':39,'english':39,'sports':93
    }},
    {'name':'john','score':{'math':94,'english':79,'sports':95}},
    {'name':'lili','score':{'math':91,'english':39,'sports':69}},
]

# 统计平均成绩分别是
for key in stu_scores:
    score_list=key['score'].values()
    # 平均值
    avg=sum(score_list)/len(score_list)
    print(f"{key['name']} average score is {avg:.1f}")

# 找到最高的分数
def find_best_score():
    best_stu=[]
    best_score=0
    for stu in stu_scores:
        total=sum(stu['score'].values())
        if total > best_score:
            best_score=total
            best_stu=[stu['name']]
        elif total == best_score:
            best_stu.append(stu['name'])
    print(f"best score is {total}, best student is {best_stu}")
find_best_score()

comment='一点点奶茶真好喝，草莓奶茶最好喝，爱喝奶茶，每天都喝一杯，价格不贵'
# 统计字符出现的次数
print(comment.count('喝'))
print(comment.replace('奶茶','咖啡'))
print( '一杯' in comment)


