#Python 獠牙运算符 :=

#獠牙运算符 可以简易使用True/False
#赋值表达式 :-
#赋值运算子 =

#Python 3.8 之后才有的

happy = True
print(happy)

print(happy := True) #用:- 可以这样写

#原本
foods=[]
while True:
    food = input("What food you like?")
    if food == "quiet":
        break
    foods.append(food)

print(foods)

#使用:=
foods=[]
while (food := input("What food you like?: ")) != "quiet": #需要放进(),不然回传值变True/False
    foods.append(food)
print(foods)
