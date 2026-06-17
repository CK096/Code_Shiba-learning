# Python 字串索引原来那么简单

credit_number = "1234-4578-9876-5432"
first_num = credit_number[0]
print("first word", first_num)

sec_num = credit_number[1]
print("Second word", sec_num)

first_four = credit_number[0:4]
print("infront four word", first_four)

last_num = credit_number[-1]
print("last word", last_num)

sec_last_num = credit_number[-2]
print("last sec word", sec_last_num)

last_four_num = credit_number[-4:-1]
print("last four word", last_four_num)

str = '123456789'

print(str)  # 输出字符串
print(str[0:-1])  # 输出第一个到倒数第二个的所有字符
print(str[0])  # 输出字符串第一个字符
print(str[2:5])  # 输出从第三个开始到第六个的字符（不包含）
print(str[2:])  # 输出从第三个开始后的所有字符
print(str[1:5:2])  # 输出从第二个开始到第五个且每隔一个的字符（步长为2）
print(str * 2)  # 输出字符串两次
print(str + '你好')  # 连接字符串