# Python 中的 Time

# 系统的初始时间 epoch

import time
print(time.ctime(0)) #把时间戳 0 转换成可读时间。系统时间戳的起点是 1970 年 1 月 1 日 00:00:00 UTC
print(time.time()) #返回当前 系统时间戳，单位是秒

#获取现在的时间
local_time = time.localtime()
print(local_time) # 这样只是输出时间的Object
print("格式化的时间: ", time.strftime("%Y-%m-%d %H:%M:%S", local_time)) #输出时间的方式，str 需要跟着写

#把str转成时间Object的方式
time_string = "1999-09-06 12:12:12"
time_object = time.strptime(time_string,"%Y-%m-%d %H:%M:%S")
print(time_object)
