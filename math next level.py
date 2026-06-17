import math
#上面的import math "(数学模块)" 代表进位进阶必要程式 (写了import math在第一行才可以用 math.ceil 或其他)

#四舍五入， 无条件进位(math.ceil)，无条件舍去(math.floor)
x = 9.5
print(round(x))
print(math.ceil(x))
print(math.floor(x))

# 圆周率 π (math.pi)
print(math.pi)
# 计算圆的周长 2πR
radius =float(input("Long"))
c = 2 * math.pi * radius
print(f"圆的周长: {round(c , 2)}")

# 计算圆的面积 πR2
radius =float(input("Long"))
c = math.pi * radius ** 2
print(f"圆的面积: {round(c , 2)}")