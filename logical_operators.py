# Python 中的逻辑运算子(运算符)

# and, or, not

#and
temp = int(input("请输入现在的温度: "))
if temp > 0 and temp <= 30:
    print("温度是合适的")
else:
    print("温度是不适宜的")

# or
if temp <=0 or temp >=30:
    print("温度是不适宜的")
else:
    print("温度是适宜的")

# not
if not temp >= 30 and temp > 10 :
    print("温度是适宜的")
else:
    print("温度是不适宜的")
