 #巢状回圈
for x in range(1,9):
    print(x,end=" ") # (end="") 等于不换行,在""加字可以跟着加
print() #加这个在(end="")下面可以换行

for y in range(5):
    for x in range(1, 10):
        print(x, end=" ")
    print()

row = int(input("请输入行数: "))
cols = int(input("请输入列数:"))
symbol = input("请输入符号: ")

for z in range(row):
    for t in range(cols):
        print(symbol,end=" ")
    print()

for j in range(1,5):
    for k in range(1,5):
        for l in range(1,5):
           if (j!=k) and (k!=l) and (j!=l):
              print(j,k,l)