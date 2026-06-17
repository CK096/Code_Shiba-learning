# Python f-string 的字串格式化
# print 的时候尾的地方放 \n 可以带入下一行

price_1 = 3.321
price_2 = -77
price_3 = 15.11

print(f'价格 1 为 {price_1}\n'
      f"价格 2 为 {price_2}\n"
      f"价格 3 为 {price_3}")

#如果后面要2位小数点就加 :.2f

print(f'价格 1 为 {price_1:.2f}\n'
      f"价格 2 为 {price_2:.2f}\n"
      f"价格 3 为 {price_3:.2f}")

# 加正数或者负数 “+”

print(f'价格 1 为 {price_1:+.2f}\n'
      f"价格 2 为 {price_2:+.2f}\n"
      f"价格 3 为 {price_3:+.2f}")

# 对齐位置 < > ^

print(f'价格 1 为 {price_1:20.2f}\n'
      f"价格 2 为 {price_2:20.2f}\n"
      f"价格 3 为 {price_3:20.2f}")

print(f'价格 1 为 {price_1:<20.2f}\n'
      f"价格 2 为 {price_2:<20.2f}\n"
      f"价格 3 为 {price_3:<20.2f}")

print(f'价格 1 为 {price_1:>20.2f}\n'
      f"价格 2 为 {price_2:>20.2f}\n"
      f"价格 3 为 {price_3:>20.2f}")

print(f'价格 1 为 {price_1:^20.2f}\n'
      f"价格 2 为 {price_2:^20.2f}\n"
      f"价格 3 为 {price_3:^20.2f}")

#混合不同符号

print(f'价格 1 为 {price_1:>+20.2f}\n'
      f"价格 2 为 {price_2:>+20.2f}\n"
      f"价格 3 为 {price_3:>+20.2f}")

#放入整数时根据你放的号码变化 列子：放04变4位数
x = 50
print(f'{x:04}')
y = 0.55 #放浮点数时不会变化哦
print(f'{y:.04}')
y = 0.55 #浮点数需要换成这样
print(f'{y:.4f}')

#如果代码很长可以用 (\)带入下一行

item_one = int(input("n1:"))
item_two = int(input("n2:"))
item_three = int(input("n3:"))

total = print(item_one ,\
              item_two ,\
              item_three)

#在 [], {}, 或 () 中的多行语句，不需要使用反斜杠 (\)例如:
item = print('item_one', 'item_two', 'item_three',
             'item_four', 'item_five')

# 使用反斜杠(\n)转义特殊字符
print('hello\nrunoob')
# 在字符串前面添加一个 r，表示原始字符串，不会发生转义
print(r'hello\nrunoob')
# (\n\n) 在结果输出前会输出两个新的空行。一旦用户按下 enter 键时，程序将退出
input("\n\nHaha放两个可以空多一行，加一个多一行。")