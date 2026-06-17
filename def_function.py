#pyhon 中的函数 / 函式(function)
#又称为方法(Method)

def say_bye(): #在 def 后面随便打字加() 整段程式呼叫的时候就可以直接套用了
    print("Goodbye")
say_bye()
say_bye()
say_bye()

def who(name): #可以传递参数
    print(f" hi ,{name}")
who("Ck")
who("Kok")


# return 可以让 X 和 Y 可以用数学
def cincai(x,y):
    return x + y
print(cincai(2,3))
result = cincai(4,5)
print(result)

def apa(x,y):
    return x - y
print(apa(2,5))
result1 = apa(12,8)
print(result1)

def lu_mau(x,y):
    return x * y
print(lu_mau(2,5))
result2 = lu_mau(2,8)
print(result2)

def i_win(x,y):
    return x / y
print(i_win(4,2))
result3 = i_win(9,3)
print(result3)

#Str 也可以加哦
def create_name(first,last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last

print(create_name("ck", "kok"))
