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
squares = [x * x for x in range(1,11)]#[表达式 for 变量 in 可迭代对象]
print(squares)


grades = [100,90,66,80,46,29,88]
passed_grades = [g for g in grades if g >= 60]
# 单纯筛选时，表达式可以直接写变量 g
# 只有符合 if 条件的元素才会加入新 List
pass_grade = [y for y in grades if y >= 60]
# 这样也可以
print(passed_grades)


names = ["alice", "BOB", "Alexander", "tom", "AMANDA"]
result = [a.upper() for a in names if len(a)>4]
print(result)
#加入内建函式也可以哦

# 写法	                                  用途
# [x * 2 for x in numbers]	              取出元素并转换
# [x for x in numbers if x > 10]	      筛选符合条件的元素
# [x * 2 for x in numbers if x > 10]	  先筛选，再转换


# 之前的if 在后面， 是为了筛选要不要保留元素
# 这里的if else 是决定要变成什么元素，所以在前面
# Example
numbers = [1, 2, 3, 4, 5]
result = ["Big" if i >=3 else "Small" for i in numbers]
print(result)

# List 生成 (List,Set,Dictionary)
students = [
    {"name": "Alice", "score": 85},
    {"name": "Bob", "score": 55},
    {"name": "Charlie", "score": 92},
    {"name": "David", "score": 48}
]
result = [student["name"] for student in students if student["score"] >= 60] #这是生成list
result2 = {student["score"] for student in students if student["score"] >= 60} #这是生成set
result3 = {student["name"]: student["score"] for student in students if student["score"] >= 60} #这是生成Dictionary
print(result)
print(result2)
print(result3)

#=================================================================================================================
#重点理解：三种推导式

#List to List Comprehension
#用 [] 创建 List
[product["price"] * 0.9 for product in products]
#结果：一组价格，保留顺序和重复值

#List to Set Comprehension
#用 {} 创建 Set
{product["price"] * 0.9 for product in products}
#结果：不重复的价格，且不保证顺序

#List to Dictionary Comprehension
#用 {key: value} 创建 Dictionary
{product["name"]: product["price"] * 0.9 for product in products}
#结果：商品名称对应折后价格

记住这个关键区别：
[expression for ...] → List Comprehension
{expression for ...} → Set Comprehension
{key: value for ...} → Dictionary Comprehension
