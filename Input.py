# input 取得使用者输入
name = input("please key in name: ")
print(f'your name is {name}')

# 练习一 ： 填词游戏
adj_1 = input("plese key in first 形容词: ")
noun = input("please key in 名词： ")
adj_2 = input("plese key in Second 形容词: ")
verb = input("please key in 动词： ")
adj_3 = input("plese key in Third 形容词: ")

print(f"今天我去了一个{adj_1}的动物园，在展览中我看到了{noun}, 这个{noun}很{adj_2},正在{verb}, 我感到很{adj_3}")

# 练习二 ： 计算矩形面积
long = float(input("矩形的长度: "))
weight = float(input("矩形的宽度: "))
area = (long*weight)

print(f"矩形的面积: {area}平方公分")


# 练习三 ： 购物车程式

item = input("想要购买的物品： ")
price = float(input("购买物品的价格： "))
quantity = int(input("购买物品的数量： "))

total = price * quantity

print(f'你购买了{quantity} {item},总价值 RM{total}')