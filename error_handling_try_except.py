# Python 中的错误处理 (Error Handling,异常处理)

#exception

try:
    x = int(input("key in Int: ")) #没有 try except 的话输入float会是一个 ValueError 的错误
    y = int(input("key in another Int: "))
    print(x/y) #没有 try except 的话输出会是一个 ZeroDivisionError 的错误
except ValueError:
    print("请输入整数")
except ZeroDivisionError:
    print("除数不能为 0")

#也可以同时输入两种错误
except (ZeroDivisionError,ValueError):
    print("输入错误，请重新输入")
else: #当出现除了except的错误才会执行else, 不过很少会用到
    print("else")
finally: #不管正确或错误，都会执行这段程式码
    print("无论有没有错误，都会执行这个")


#exp
inventory = {
    "Mouse": 15,
    "Keyboard": 8,
    "Monitor": 3
}

item = input("Enter Product Name: ").title()
if item in inventory:
    print(f"this product on store now has {inventory[item]}")
else:
    print("Product Not Found")
    exit()
try:
    qty = int(input("Qty your want to Buy: "))
except ValueError:
    print("Invalid Number")
else:
    if qty > inventory[item]:
        print("Qty no enough")
    elif qty <= 0:
        print("Qty Cant Less then 0")
    else:
        inventory[item] -= qty
        print(f"Thanks For your Buying\nRemaining Stock {inventory[item]}")
