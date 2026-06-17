# String 字符串，字母
name = "CK"
print(f'my name is {name}')
print(type(name))

#允许多个变量赋值
a = b = c = 1
a, b, c = 1, 2, "runoob"

# integer 整数
x = 11+7
y = 6
print(x)
print(x+y)
print('My age is',(x+y))
print(type(x+y))
# Float 小数点
gpa = 3.3
print(gpa)
print(f'my gpa is {gpa} mark')
print(type(gpa))
# integer+ Float
print(f'my friend is {x+y + gpa} mark')
print(type(x+y + gpa))
print(f'my friend is {x+y} mark')
print(type(x+y))
# String + Integer + Float
print(f'Student {name} is {x*y + gpa} mark')
#Boolean # True, False
Pass = True
print(f"Student {name} is {x*y + gpa} mark is {Pass}")
print(type(Pass))
# 不换行输出
print(x, end=" ")
print(y, end=" ")
print()