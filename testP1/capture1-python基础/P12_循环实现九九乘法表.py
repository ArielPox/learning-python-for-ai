print("print会自带一个换行的 可以使用end=""来控制不换行")

for i in range(1,10):
    for j in range(1,i+1):
        print(f"{i}*{j}={i*j}",end=" ")
    print()    