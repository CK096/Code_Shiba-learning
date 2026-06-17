# Python 中的作用域

# 变数范围与作用域
# LEGB 作用域顺序

# L - local 区域
# E - Enclosed
# G - Global 全域
# B - Build in


# 变数范围
c = 10 #这个属于 G-global全域 (全部范围都可用)
a = 6 #这个不会显示在function_one 里面，因为function_one 是一个（local-区域）
def function_one():
    a = 1 #function_one 的 local 区域
    print("a: ",a)
    def function_two():
        b = 2 #function_two 的 local 区域
        print("a: ",a) # 放在function_two的时候原本的function_one 的 (a)是 E-enclosed
        print("b: ",b)
        print("c: ", c)
    function_two()

function_one()
print("global A:", a) #这个不是调用function_one(local-区域)，所以a是最开始那个

from math import e
print(e)
print(round(e))

def function_three():
    print(e)
function_three()