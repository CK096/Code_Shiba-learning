# Python 中的列表推导式（List Comprehension）

# 列表推导式 => 更少的语法创建新列表

#普通写法
def square(x):
    return x * x
numbers = []
for i in range(1,11):
    numbers.append(square(i))
print(numbers)

# 列表推导式
# [表达式 for 变量 in 可迭代对象]
# x * x (表达式)
# for x in range(1, 11)：逐个取出数字
# 外面的 []：创建新的 List
square = [x * x for x in range(1,11)]#[表达式 for 变量 in 可迭代对象]
print(square)


grades = [100,90,66,80,46,29,88]
passed_grades = [g for g in grades if g >= 60]
# 单纯筛选时，表达式可以直接写变量 g
# 只有符合 if 条件的元素才会加入新 List
pass_grade = [y for y in grades if y >= 60]
# 这样也可以
print(passed_grades)

# 写法	                                  用途
# [x * 2 for x in numbers]	              取出元素并转换
# [x for x in numbers if x > 10]	      筛选符合条件的元素
# [x * 2 for x in numbers if x > 10]	  先筛选，再转换
