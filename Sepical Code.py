print #输出
input #输入
str # string 字符串 # exp: "Mr Handsome"
int #interger 整数的缩写 #exp: 16
float # float 浮点数 #exp: 3.123
if # 如果某回答这样， 就。。。
elif # 或者某回答那样， 就。。。 #elif 可以一直叠加
else  # 其他答案的话
while # 当需要循环的时候，可以使用这个

for # 当有固定次数的循环时，用这个更好
in # 放入可以迭代的东西，例如数字
range # 放入可以迭代的东西之间，例如数字
reversed # 可以用来倒数
continue # 继续的意思，不过会Skip 掉你选的那个字
break # 会停止到你写的那个字
items() # 导出键与值
end="" # 在每一个的尾部加多一个字， ""写在这里面

#example:
for x in reversed(range(10)):
    print(x,end="")
A = "IC = 990906-10-3479"
for c in A:
    if c == "1":
        continue #continue 换成break 可以停止到你选的字
    print(c)

#字典 Dictionary
# “A” = key(键)， 1 = Value(值)
disc = {"A":1,"b":2,"c":3}
print(disc) # 这个只是输出整个disc而已
print(disc["a"]) #输出Value

disc = {"A":1,"b":2,"c":3}
for x in disc:
    print(x) #输出所有的Key

disc = {"A":1,"b":2,"c":3}
for key,value in disc.items(): #items() 导出键与值
    print("Key", key)
    print("Value", value)


True # Bool true 布林值为真
False # Bool false 布林值为假
and # 如果两边的问题答案都是 true， 回答为true,
or # 如果两边的问题其中一个答案是 true， 回答为true,
not # 如果问题的答案是False，回答为true， 通常放在if/else 的后面，变量的前面
!= # 这是不等于的意思
in # 当某个东西在里面，需要标注并使用它时使用， exp: if "A" in name:
+ - * / % # 加 减 乘 除 余数
max # 取数字最大值
min # 取数字最小值
round # 把有小数点的号码进位
round(a, 2) #进位为小数点二位数 # a 只是变数例子
pow # 平方次使用(2x2x2 = 2,3) (5x5x5 = 5,3)
len # 计算有多少字
count # 计算指定的字有多少个
.replace(" "," ") #可以换掉的字, 第一个是原本的字，第二个是要替换掉的字
.find() # 寻找某个字在第几个位子，()里面要填要找的东西
.upper() # 无条件把字符串(字母)换成大写
.lower() # 无条件把字符串(字母)换成小写
.capitalise() # 把第一个字母变大写
.isalpha() # 询问是否为全部字母， 不包含数字，符号

字符搜索 #用[]
A = "1234567890"
first word = A[0] #搜索从0开始，左到右
last word = A[-1] # 搜索从最后开始，右到左
between = A[1,4] # 搜索字从哪开始，到哪结束
after = A[2:]   # 搜索整段哪个位之后的字
Before = A[:6]   # 搜索整段哪个位之前的字

字符解析
gmail = "ckkok@gmail.com"
.index() # 可以找字符在哪个位子 #EXP:  AB = gmail.index("@")
print(gmail[:AB]) # 搜索整段那个位之前的字
print(gmail[AB+1:]) # 搜索整段那个位之后的字(因为+1所以会跳过“@”这个字符)

#这是list (用 [])
fruit = ["apple", "banana", "cherry"]
fuit.append("orange") # .append()是加入东西
fruits.append("orange") #在List里面重复的东西是可以加入的,会出现在最后 (只可以用在list)
fruits.count("orange") # 可以计算有多少一样的在里面
fruit.remove("banana") # .remove 是移除东西
fruit.reverse() # 倒反可以哦
food.index("cherry") # .index() 索引也可以用哦

#set 列表 (需要使用大栝号{}) #set 是不能重复而且没有顺序的
fruit = {"apple", "banana", "cherry"}
fruit.add("orange") #set 的加入方式

# tuple 元组 (由栝弧组成的(),有秩序的并且内容不能改变)
fruits_tuple = ("Durian","Watermelon","Pineapple","Papaya")
Result = fruits_tuple.count("Durian")
result = fruits_tuple.index("Papaya")

# Python 字典入门
#键 => 值 (key => value) (键值对) (具有顺序性还有可变性,Key 不可以重复)
capital = {"United States": "Washington DC", #嫌弃太长的话可以这样写
           "Japan": "Tokyo",
           "France": "Paris",
           "Russia": "Moscow"}

#.get() 可以取得你键值对
print(capital.get("Japan"))
print(capital.get("France"))
#.update() 更新/加入键值对
capital.update({"Malaysia": "Kuala Lumpur"}) #需要放{}
print(capital.get("Malaysia"))
#.pop() 删除键值对
capital.pop("United States") #不需要放{}
print(capital)
#.values() 获得所有值
print(capital.values())
#.items() 获得所有键值对
print(capital.items())


import math #数学模块 (以下是他的模组)
math.pi # 数学圆的Pi
math.ceil # 无条件小数点进位
math.floor #无条件小数点不进位

import time #时间模组
time.sleep() #延迟暂时，在()里面写号码就可以延迟几久

import random
randint() #显示随机号码
print(random.randint(1,10))
random() #显示随机浮点数
print(random.random())
#列表中随机一个元素
option = ["石头","剪刀","布"]
rand_option = random.choice(option)
print(rand_option)

#把一个列表打乱
card = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
random.shuffle(card)
print(card)
