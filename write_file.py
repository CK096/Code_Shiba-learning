# Python 写入档案

str = r"C:\Users\user\Desktop\workshop\learn.txt"

text = "keat is handsome \nand he was rich"

#以下两个方式都可以生成档案，用现在的str(变数)路径换后面的名字可以生成文件
#测试的时候记得其中一个换成#注释

# w 模式 (一次输入的模式)
with open(str,"w") as file: # with open(str,"w") (记得放"w")
    file.write(text)

# a 模式 (加入写入现有文件的模式)
with open(str,"a") as file: # with open(str,"a") (记得放"a")
    file.write(text)