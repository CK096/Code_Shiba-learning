# Python 中的 while 循环圈

# 当输入到某个指定的答案时需要修改是会执行回重复的操作 = while
name = input("请输入你的名字")
while name == "":
    name = input("请输入你的名字")
print(f"你好{name}")

name = ""
while name == "":
    name = input("请输入你的名字")
print(f"你好{name}")

# 等于用 = ， 不等于用 !=

food = input("你喜欢的食物是什么: ")
while food != "q":
    print(f"你喜欢的食物是{food}")
    food = input("你喜欢的食物是什么: ")
print("再见")

num = int(input("请输入 1 到 10 的整数"))
while num < 1 or num > 10:
    print(f"你输入的{num}是无效的")
    num = int(input("请输入 1 到 10 的整数"))
print(f"你要的数字是{num}")