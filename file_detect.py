# 使用 Python 进行档案检测

import os  #使用os模组

str = r"C:\Users\user\Desktop\workshop" #前面放r可以把\也算进去
stt = "C:\\Users\\user\\Desktop\\workshop" #换成\\也有一样的效果哦
print(str)
print(stt)

if os.path.exists(str): #os.path.exists()检测该路径是否存在你的电脑
    print("路径存在！")
else:
    print("路径不存在！")

if os.path.isfile(str): #os.path.isfile()检测该路径是否为档案
    print("该路径为档案")
elif os.path.isdir(str): #os.path.isfile()检测该路径是否为目录
    print("该路径为目录")
else:
    print("other")