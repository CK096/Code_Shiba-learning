weight = float(input("请输入你的体重： "))
unit = input("你的体重要换算成公斤还是磅？(kg/lbs)： ").upper()

while unit != "KG" and unit != "LBS":
    unit = input("Please Key Correct Unit: ").upper()

## .upper() (放在input句子后面可以把字串变成大写)

# 第一个方法
if unit == "KG":
    weight /= 2.2
    print(f"你换算的单位结果是: {(round(weight, 2))} KG")

elif unit == "LBS":
    weight *= 2.2
    print(f"你换算的单位结果是: {(round(weight, 2))} LBS")
else:
    print("请输入正确的单位换算！")

#第二个方法
if unit == "KG":
    weight /= 2.2
    new_unit = "公斤"
elif unit == "LBS":
    weight *= 2.2
    new_unit = "磅"
else:
    print("请输入正确的单位换算！")
    exit()

print(f"你换算的单位结果是: {(round(weight, 2))} {new_unit}")

