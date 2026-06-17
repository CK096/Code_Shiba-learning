#显式型别转换
name = 'Ck'
age = 25
mark = 99.99
gamer = True

ages = float(age)
print("my age is " , (ages))
print(type(ages))

marks = int(mark)
print(f"my age is {mark}")
print(type(marks))

gamers = str(gamer)
print('i was gamer '+ str(gamers))
print(type(gamers))

#隐式型别转换
x = 10
y = 2.0
x = x*y
y = x+x
print(y)
print(type(y))