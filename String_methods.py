# python 各种字串用法

name = "mrCK"

# 计算总共多少个字 = len ("输入想要计算的字代表”)
lenght = len(name)
print("Your name have", lenght ,"word")

# 找到第一个想要的字符的位置 = .find(“输入要找的字符”)
space_pos = name.find("C")
print("the first space on", space_pos ,"word")

# 让第一个字变成大写 = .capitalize()
name_capitalized = name.capitalize()
print("the capitalize your name is", name_capitalized,)

# 让所有字都变大写 = .upper()
name_upper = name.upper()
print("Change your name all to upper:", name_upper,)

# 让所有字都变小写 = .lower()
name_lower = name.lower()
print("Change your name all to lower:", name_lower,)

# 计算你想要找的字符串有几个= .count(”输入想要找的字符“)
phone_number = input("Pleas Enter Your Phone Number")
dash_count = phone_number.count("-")
print("your phone total have", dash_count,"(-)")

# 换掉你想换的字 = .replace("你想换掉的","你想输入代替换掉的")
phone_number = phone_number.replace("-", "xx")
print("your phone number - change to xx:", phone_number)

# 计算是否全是英文字 = .isalpha()
if name.isalpha():
    print("your name all is english")
else:
    print("your name have other")

# 包含 = "输入要的字" in
if "CK" in name :
    print("yes")
else:
    print("no")

#题目练习
# - 您的使用者名称不能超过12个字
# - 您的使用者名称不能包含空格
# - 您的使用者名称不能包含数字
# - 如果都符合的话, 显示: 欢迎 + 使用者名称

username=input("请输入你想要的名字:")


if len(username) > 12 :
    print("您的使用者名称不能超过12个字")
elif " " in username :
    print("您的使用者名称不能包含空格")
elif not username.isalpha():
    print("您的使用者名称不能包含数字")
else:
    print("欢迎您: " + username)

# 使用反斜杠(\n)转义特殊字符
print('hello\nrunoob')
# 在字符串前面添加一个 r，表示原始字符串，不会发生转义
print(r'hello\nrunoob')
# (\n\n) 在结果输出前会输出两个新的空行。一旦用户按下 enter 键时，程序将退出
input("\n\n放两个可以空多一行，加一个多一行。")