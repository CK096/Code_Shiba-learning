#Python 中的集合 list, tuple, sets

#list 列表 (需要使用方栝号[]) #list 是有顺序而且可以重复的

fruits = ["Apple","Orange","Banana","Grape"]

print(fruits) #这样可以显示出想要的东西
print(fruits[2]) #顺序是从 0 开始的，这样可以显示出特定的东西 #这样是横着（一行）显示

for f in fruits: #这样是竖着（换行）显示
    print(f)

fruits.append("Peach")#append.("x") 这个英文是加入的意思
print(fruits)

fruits.append("Grape") #在List里面重复的东西是可以加入的,会出现在最后 (只可以用在list)
print(fruits)
print(fruits.count("Grape")) # .count("x")计算有多少
print(fruits.index("Grape")) # .index("x")搜索位置

fruits.remove("Apple") #remove.("x") 这个英文是移除的意思
print(fruits)

fruits.reverse() #倒着列出来
print(fruits)

if "Grape" in fruits:
    print("Here Have Grape")

#set 列表 (需要使用大栝号{}) #set 是不能重复而且没有顺序的
fruits_set_A = {"🍒","🍓","🍅","🍐"}
fruits_set_B = {"Peach","Strawberry","Tomato","Pear"}
for s in fruits_set_A:
    print(s,end="")
fruits_set_A.add("🍍") #在Set里面重复的东西是可以加入的,会出现在最后 (只可以用在Set)
print(fruits_set_A)

if "🍒" in fruits_set_A:
    print("这是一个樱桃")

# tuple 元组 (由栝弧组成的(),有秩序的并且不能改变)
fruits_tuple = ("Durian","Watermelon","Pineapple","Papaya")
Result = fruits_tuple.count("Durian")
print(Result)
result = fruits_tuple.index("Papaya")
print(result)