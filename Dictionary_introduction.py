# Python 字典入门
#键 => 值 (key => value) (键值对) (具有顺序性还有可变性,Key 不可以重复)

capital = {"United States": "Washington DC", #嫌弃太长的话可以这样写
           "Japan": "Tokyo",
           "France": "Paris",
           "Russia": "Moscow"}

#.get() 可以取得你键值对
print(capital.get("Japan"))
print(capital.get("France"))

#.update() 更新键值对
capital.update({"Malaysia": "Kuala Lumpur"}) #需要放{}
print(capital.get("Malaysia"))
.update() 有两个用途：#可以一直增加
如果 key 不存在 → 新增
如果 key 已存在 → 修改

capital["Thailand"] = "Bangkok" #这样也可以加(from GPT)
print(capital.get("Thailand"))

#.pop() 删除键值对
capital.pop("United States") #不需要放{}
print(capital)

#.values() 获得所有值
print(capital.values())

#.items() 获得所有键值对
print(capital.items())
