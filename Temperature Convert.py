unit = input("当前的温度单位(摄氏度 C,华氏度 F): ").upper()
temp = float(input("请输入当前的温度： "))

if unit == "C":
    temp = 9 * temp / 5 +32
    new_unit = "F，华氏度"
if unit == "F":
    temp = (temp - 32) * 5 / 9
    new_unit = "C，摄氏度"
else:
    print("请输入正确的单位")
    exit()

print(f"转换之后的单位： {round(temp,1)}{new_unit}")

