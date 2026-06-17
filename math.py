# 加减乘除
apples = 3
apples = apples + 1
apples += 1
print(apples)
apples = apples - 1
print(apples)
apples -= 1
print(apples)
apples = apples * 2
print(apples)
apples *= 2
print(apples)
apples = apples / 2
print(apples)
apples /= 2
print(apples)
# 指数 (平方， 三次方)
apples = 3
apples = apples ** 3
print(apples)
apples = apples ** 3
apples **= 3
print(apples)

# 模数 (mod) (除法剩下的余数)
# 10 mod 除 3 剩 1
print(10 % 3)
# 11 mod 除 3 剩 2
print(11 % 3)
# 12 mod 除 3 剩 0
print(12 % 3)

# 内置数学函数
# 次方 pow
print(pow(2,3))
print(pow(4,3))

# 最大值 Max 与最小值 Min
x = 99
y = 76
z = 69
print(max(x,y,z))
print (min(x,y,z))

# 四舍五入 round
a = 3.14
print(round(a))
b = 3.5
print(round(b))

### 绝对值 abs (把负数去掉)
c =-56
print(abs(c))