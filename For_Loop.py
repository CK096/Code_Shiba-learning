#Python 中的 for 循环

# (in) 后面要放可以迭代的
# (range) 可以产生可以迭代的东西
for x in range(1,11):
    print(x)
# 要倒转的话可以加入 (reversed)
for y in reversed(range(1,11)):
    print(y)

credit_card = "1234-5678-9012-3456"
for a in credit_card:
    if a == "9":
        continue #用continue可以跳过那个字符串
        break #用break 可以中断后面的字符串
    print(a)

#字典 Dictionary (需要使用大栝弧{}，里面需要包含字符串和数值)
# 字符串 = 键 = key, 数值 = 值 = Value
my_dict = {"a": 1,"b":2,"c":3}
for z in my_dict:
    print(z) #这样只会迭代 “键” 而已
for C, D in my_dict.items(): #加入item.()可以在前面迭代两个变量，把Key和value一起拉出来
    print("key: ",C)
    print("Value: ", D)

