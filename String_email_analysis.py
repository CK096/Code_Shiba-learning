# Email 字串分析

#搜索在在第几个位置 = .index("要找的字串")
#
email = "chunkeat990906@gmail.com"
index = email.index("@")

print(index)
print(email[0:index])
print(email[:index])
print(email[index:])
print(email[(index+1):])
print(email[(index+1):-1])