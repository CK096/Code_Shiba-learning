# Python 中的 Lambda

# Lambda 有函式的功能，一行就能写完

#以下是平常用的函式
def double(x):
    return x * 2

print(double(4))

#ex1 普通lambda
double2 = lambda x: x*2
print(double2(50))

#ex2 复数处理
multiply = lambda x, y:x*y
print(multiply(2,10))

#ex3 if else 条件语句
result = lambda x:f"{x} 是偶数" if x % 2 == 0 else f"{x} 是奇数"
print(result(9))

#ex4 字串处理
full_name = lambda first_name,last_name: f"{first_name} {last_name}"
print(full_name("Im","Rich"))
