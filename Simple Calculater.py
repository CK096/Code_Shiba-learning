number_1 = float(input("请输入第一个号码"))
operator = input("请输入运算符号，加法: + ,减法: -,乘法: *,除法: /")
number_2 = float(input("请输入第二个号码"))


if operator == "+":
    Result = (number_1 + number_2)
elif operator == "-":
    Result = (number_1 - number_2)
elif operator == "*":
    Result = (number_1 * number_2)
elif operator == "/":
    Result = (number_1 / number_2)
else:
  print("Sorry,我太菜算不出来，你行你上")

print(f"运算结果是{Result}")

Long = float(input("Long:"))
Lenght = float(input("Lenght:"))
Height = float(input("Height:"))
count = input("请输入需要计算的单位: 面积(surface), 体积(result)")
result = Long * Lenght * Height
surface = Long * Lenght

if count == "result":
    print(f"立体的答案是{result}")
elif count == "surface":
    print(f"面积的答案是{surface}")
else:
    print("不好意思找不到你要的答案")
