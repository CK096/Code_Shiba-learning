# Python 读取档案
str = r"C:\Users\user\Desktop\workshop\test.txt"
try:
    with open(str) as file:
        print(file.read())
except FileNotFoundError:
    print("该档案不存在")