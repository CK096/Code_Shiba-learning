# 复利计算机
# 总金额 = 本金 * (1 + (利率/100)) ** 时间

amount = 0
interest = 0
year = 0

while amount <= 0:
    amount = float(input("请输入你的本金: "))
    if amount <= 0:
        print("本金不可以小于零!")

while interest <= 0:
    interest = float(input("请输入你的利率: "))
    if interest <= 0:
        print("利率不可以小于零!")

while year <= 0:
    year = int(input("请输入你要放的时间: "))
    if year <= 0:
        print("最少要存放1年!")

print("您的金额是:",amount)
print("您的年利率是:",interest)
print("您要存放多少年:",year)

total = amount * (1 + interest / 100) ** year

print("总金额:", (round(total,2)))