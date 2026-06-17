# if, else, elif 控制流程

# Boolean 布林值
boss = True
if boss :
    print("good boos")
else:
    print("Strong Staff")
boss = False
if boss:
    print("good boss")
else:
    print("Strong Staff")

#if (如果是xx), else(如果是其他)
age = int(input("请输入你的年龄"))

if age >= 18:
    print("你符合购买资格")
else:
    print("你不符合资格购买")

#elif (额外情况的话)
age = int(input("请输入你的年龄"))

if age >= 100:
    print("不适合您的年龄购买")
elif age >= 18:
    print("你符合资格购买")
elif age < 12:
    print("请回去找家人，不要捣乱")
else:
    print("你不符合资格购买")